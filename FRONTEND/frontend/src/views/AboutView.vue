<template>
  <table align="left">
    <h1>Agregar Docente</h1>
    <tr>
      <th scope="col">Cedula</th>
      <th scope="col">Nombre</th>
      <th scope="col">Apellido</th>
      <th scope="col">Correo</th>
      <th scope="col">Telefono</th>
    </tr>
    <tr>
      <td>
        <input type="text" id="doc_cedula" name="doc_cedula" v-model="doc_cedula">
      </td>
      <td>
        <input type="text" id="doc_nombre" name="doc_nombre" v-model="doc_nombre">
      </td>
      <td>
        <input type="text" id="doc_apellido" name="doc_apellido" v-model="doc_apellido">
      </td>
      <td>
        <input type="text" id="doc_correo" name="doc_correo" v-model="doc_correo">
      </td>
      <td>
        <input type="text" id="doc_telefono" name="doc_telefono" v-model="doc_telefono">
      </td>
    </tr>
    <tr>
      <button v-on:click="registrar()">Crear</button>
    </tr>
    <br><br><br>
    <h1>Listado de Docentes</h1>
    <tr>
      <th scope="col">Cedula</th>
      <th scope="col">Nombre</th>
      <th scope="col">Apellido</th>
      <th scope="col">Correo</th>
      <th scope="col">Telefono</th>
    </tr>
    <tr v-for="i in Lista">
      <td>{{ i.doc_cedula }}</td>
      <td>{{ i.doc_nombre }}</td>
      <td>{{ i.doc_apellido }}</td>
      <td>{{ i.doc_correo }}</td>
      <td>{{ i.doc_telefono }}</td>
      <td>
        <button v-on:click="eliminar(i.doc_cedula)">Eliminar</button>
      </td>
      <td>
        <button v-on:click="editar(i.doc_cedula)">Actualizar</button>
      </td>
    </tr>
  </table>
</template>
<script>
  import axios from 'axios';

  export default {
    name: "AboutView",
    data() {
      return {
        Lista: null,
        doc_cedula: "",
        doc_nombre: "",
        doc_apellido: "",
        doc_correo: "",
        doc_telefono: "",
      }
    },
    methods: {
      registrar() {
        let POST = {
          "doc_cedula": this.doc_cedula,
          "doc_nombre": this.doc_nombre,
          "doc_apellido": this.doc_apellido,
          "doc_correo": this.doc_correo,
          "doc_telefono": this.doc_telefono,
        }
        axios.post("http://127.0.0.1:8000/api/docente/", POST)
            .then(result => {
              this.doc_cedula="";
              this.doc_nombre="";
              this.doc_apellido="";
              this.doc_correo="";
              this.doc_telefono="";
              this.updated()
            })
      },
      editar(doc_cedula) {
        console.log(doc_cedula)
        this.$router.push('edit/' + doc_cedula);
      },
      eliminar(doc_cedula) {
        console.log(doc_cedula)
        axios.delete("http://127.0.0.1:8000/api/docente/" + doc_cedula + "/").then(result => {
          this.updated()
          console.log(result);
        })
    },
    updated() {
      let direccion = "http://127.0.0.1:8000/api/docente/";
      axios.get(direccion).then(data => {
        this.Lista = data.data;
      })
    },
  },
  mounted() {
    let direccion = "http://127.0.0.1:8000/api/docente/";
    axios.get(direccion).then(data => {
      this.Lista = data.data;
      console.log(data);
    })
  },
}
</script>

<style>

text{
  color: black;
}

button {
	background-color: rgb(123, 0, 255);
	color: #FFF;
	font-weight: 700;
	padding: 1rem 2rem;
	border-radius: 0.5rem;
	cursor: pointer;
} 

input {
	appearance:initial;
	border:blueviolet;
	outline:invert;
	background:lightpink;
	display: block;
	width: 100%;
	max-width: 400px;
	margin: 0 auto;
	font-size: 20px;;
	margin-bottom: 2rem;
	padding: 0.5rem 0rem;
}

</style>