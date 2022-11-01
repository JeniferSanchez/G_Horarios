<template>
    <table align="left">
      <h1>Actualización Docente</h1>
      <tr>
        <th scope="col">Cedula</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
      </tr>
      <tr>
        <td>
          <input type="text" id="doc_cedula" name="doc_cedula" v-model="Lista.doc_cedula">
        </td>
        <td>
          <input type="text" id="doc_nombre" name="doc_nombre" v-model="Lista.doc_nombre">
        </td>
        <td>
          <input type="text" id="doc_apellido" name="doc_apellido" v-model="Lista.doc_apellido">
        </td>
        <td>
          <input type="text" id="doc_correo" name="doc_correo" v-model="Lista.doc_correo">
        </td>
        <td>
          <input type="text" id="doc_telefono" name="doc_telefono" v-model="Lista.doc_telefono">
        </td>
      </tr>
      <tr>
      <button v-on:click="editar()">Actualizar</button>
      </tr>
    </table>
</template>
<script>
  import axios from 'axios';

  export default {
    name: "Edit",
    data() {
        return {
            Lista: [],
        }
    },
    methods: {
        editar() {
            let POST = {
                "doc_cedula": this.Lista.doc_cedula,
                "doc_nombre": this.Lista.doc_nombre,
                "doc_apellido": this.Lista.doc_apellido,
                "doc_correo": this.Lista.doc_correo,
                "doc_telefono": this.Lista.doc_telefono,
            }
            axios.put("http://127.0.0.1:8000/api/docente/" + this.$route.params.doc_cedula + "/", POST)
            .then((result)=> {
               console.log(result);
               this.Lista.doc_cedula="";
               this.Lista.doc_cedula="";
               this.Lista.doc_cedula="";
               this.Lista.doc_cedula="";
               this.Lista.doc_cedula="";
            })
        },
    },
    mounted() {
        let doc_cedula = this.$route.params.doc_cedula;
        let direccion = "http://127.0.0.1:8000/api/docente/"
        axios.get(direccion + doc_cedula).then(data => {
            this.Lista = data.data;
        })
    },
  }
</script>
