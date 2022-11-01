<template>
    <table align="left">
      <h1>Agregar Coordinador</h1>
      <tr>
        <th scope="col">Cedula</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
      </tr>
      <tr>
        <td>
          <input type="text" id="coor_cedula" name="coor_cedula" v-model="coor_cedula">
        </td>
        <td>
          <input type="text" id="coor_nombre" name="coor_nombre" v-model="coor_nombre">
        </td>
        <td>
          <input type="text" id="coor_apellido" name="coor_apellido" v-model="coor_apellido">
        </td>
        <td>
          <input type="text" id="coor_correo" name="coor_correo" v-model="coor_correo">
        </td>
        <td>
          <input type="text" id="coor_telefono" name="coor_telefono" v-model="coor_telefono">
        </td>
      </tr>
      <tr>
        <button v-on:click="registrar()">Crear</button>
      </tr>
      <br><br><br>
      <h1>Listado de Coordinadores</h1>
      <tr>
        <th scope="col">Cedula</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
      </tr>
      <tr v-for="i in Lista">
        <td>{{ i.coor_cedula }}</td>
        <td>{{ i.coor_nombre }}</td>
        <td>{{ i.coor_apellido }}</td>
        <td>{{ i.coor_correo }}</td>
        <td>{{ i.coor_telefono }}</td>
        <td>
          <button v-on:click="eliminar(i.coor_cedula)">Eliminar</button>
        </td>
        <td>
          <button v-on:click="editar(i.coor_cedula)">Actualizar</button>
        </td>
      </tr>
    </table>
  </template>
  <script>
    import axios from 'axios';
  
    export default {
      name: "Coordinador",
      data() {
        return {
          Lista: null,
          coor_cedula: "",
          coor_nombre: "",
          coor_apellido: "",
          coor_correo: "",
          coor_telefono: "",
        }
      },
      methods: {
        registrar() {
          let POST = {
            "coor_cedula": this.coor_cedula,
            "coor_nombre": this.coor_nombre,
            "coor_apellido": this.coor_apellido,
            "coor_correo": this.coor_correo,
            "coor_telefono": this.coor_telefono,
          }
          axios.post("http://127.0.0.1:8000/api/coordinador/", POST)
              .then(result => {
                this.coor_cedula="";
                this.coor_nombre="";
                this.coor_apellido="";
                this.coor_correo="";
                this.coor_telefono="";
                this.updated()
              })
        },
        editar(coor_cedula) {
          console.log(coor_cedula)
          this.$router.push('editCoor/' + coor_cedula);
        },
        eliminar(coor_cedula) {
          console.log(doc_cedula)
          axios.delete("http://127.0.0.1:8000/api/coordinador/" + coor_cedula + "/").then(result => {
            this.updated()
            console.log(result);
          })
      },
      updated() {
        let direccion = "http://127.0.0.1:8000/api/coordinador/";
        axios.get(direccion).then(data => {
          this.Lista = data.data;
        })
      },
    },
    mounted() {
      let direccion = "http://127.0.0.1:8000/api/coordinador/";
      axios.get(direccion).then(data => {
        this.Lista = data.data;
        console.log(data);
      })
    },
  }
  </script>