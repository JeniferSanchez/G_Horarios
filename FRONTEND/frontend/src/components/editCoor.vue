<template>
    <table align="left">
      <h1>Actualización Coordinador</h1>
      <tr>
        <th scope="col">Cedula</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
      </tr>
      <tr>
        <td>
          <input type="text" id="coor_cedula" name="coor_cedula" v-model="Lista.coor_cedula">
        </td>
        <td>
          <input type="text" id="coor_nombre" name="coor_nombre" v-model="Lista.coor_nombre">
        </td>
        <td>
          <input type="text" id="coor_apellido" name="coor_apellido" v-model="Lista.coor_apellido">
        </td>
        <td>
          <input type="text" id="coor_correo" name="coor_correo" v-model="Lista.coor_correo">
        </td>
        <td>
          <input type="text" id="coor_telefono" name="coor_telefono" v-model="Lista.coor_telefono">
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
    name: "editCoor",
    data() {
        return {
            Lista: [],
        }
    },
    methods: {
        editar() {
            let POST = {
                "coor_cedula": this.Lista.coor_cedula,
                "coor_nombre": this.Lista.coor_nombre,
                "coor_apellido": this.Lista.coor_apellido,
                "coor_correo": this.Lista.coor_correo,
                "coor_telefono": this.Lista.coor_telefono,
            }
            axios.put("http://127.0.0.1:8000/api/coordinador/" + this.$route.params.coor_cedula + "/", POST)
            .then((result)=> {
               console.log(result);
               this.Lista.coor_cedula="";
               this.Lista.coor_cedula="";
               this.Lista.coor_cedula="";
               this.Lista.coor_cedula="";
               this.Lista.coor_cedula="";
            })
        },
    },
    mounted() {
        let coor_cedula = this.$route.params.coor_cedula;
        let direccion = "http://127.0.0.1:8000/api/coordinador/"
        axios.get(direccion + coor_cedula).then(data => {
            this.Lista = data.data;
        })
    },
  }
</script>