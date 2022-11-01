<template>
<div class="login-container" id="container">
	<div class="form-container sign-in-container">
		<form action="" method="POST">
			<h1>Inicia Sesión</h1>
			<br><br><br>
            <div class="form-group row p-5 m-5">
                <label for="user_usuario" class="col-sm-2 col-form-label">Usuario:</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control border-success" id="user_usuario" placeholder="Ingrese usuario" v-model="login.user_usuario">
                    <label for="user_clave" class="col-sm-2 col-form-label">Contraseña:</label>
                    <div class="col-sm-10">
                    <input class="form-control border-success" placeholder="Ingrese contraseña" id="user_clave" type="password" v-model="login.user_clave">
                	</div>
                </div>
            </div>
			<a href="#" class="reset">¿Olvidó su contraseña?</a>
			<button type="submit">Ingresar</button>

		</form>
	</div>
	<div class="overlay-container">
		<div class="overlay">
			<div class="overlay-panel overlay-left">
			</div>
			<div class="overlay-panel overlay-right">
				<h1 class="login-text">SISTEMA DE GESTION DE HORARIOS</h1>
				<br><br><br>
				<h2>BIENVENIDO</h2>
				<p></p>
			</div>
		</div>
	</div>
</div>
</template>

  <script>
  import VueJwtDecode from "vue-jwt-decode";
  import swal from "sweetalert";
  export default {
    data() {
      return {
        login: {
          user_usuario: "",
          user_clave: "",
        },
      };
    },
    methods: {
      async loginUser() {
        try {
          let response = await this.$http.post("api_generate_token/", this.login);
          let token = response.data.accessToken;
          localStorage.setItem("jwt", token);
          let decoded = VueJwtDecode.decode(token);
          console.log("holadecode", decoded);
          if (token) {
            let token = localStorage.getItem("jwt");
            let decoded = VueJwtDecode.decode(token);
            swal("Exitoso", "Bienvenido " + decoded.name, "success");
            this.$router.push("/Inicio");
          }
        } catch (error) {
          swal("Error", "Este registro no existe", "error");
        }
      },
    },
  };
  </script>
  <style lang="css">

:root{
	/* COLORES */
	--color-five: #a200ff;
	/* SIZING */
	--width: 250px;
	--padding: 10px;
	--width-collapsed: 50px;
	--text-align: center;

}

    p {
	font-size: 14px;
	font-weight: 100;
	line-height: 20px;
	letter-spacing: 0.5px;
	margin: 20px 0 30px;
}

.form-container a {
	color: #333;
	font-size: 14px;
	text-decoration: none;
	margin: 30px 0;
}

.form-container form {
	background-color: #FFFFFF;
	display: flex;
	align-self: center;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 50px;
	height: 100%;
	text-align: center;
}

.login-container {
	background-color: #fff;
	position: absolute;
	top: auto;
	left: auto;
	width: 100%;
	height: 100%;
	overflow: hidden;
	z-index: 50;
}

.form-container {
	position: absolute;
	top: 0;
	left: 0;
	width: 50%;
	height: 100%;
	overflow: hidden;
	transition: all 0.6s ease-in-out;
	z-index: 100;
}


.login-container.right-panel-active .sign-in-container {
	transform: translateX(100%);
}


.login-container.right-panel-active .sign-up-container {
	transform: translateX(100%);
	opacity: 1;
	z-index: 5;
	animation: show 0.6s;
}

@keyframes show {
	0%, 49.99% {
		opacity: 0;
		z-index: 1;
	}
	
	50%, 100% {
		opacity: 1;
		z-index: 5;
	}
}

.overlay-container {
	position: absolute;
	top: 0;
	left: 50%;
	width: 50%;
	height: 100%;
	overflow: hidden;
	transition: transform 0.6s ease-in-out;
	z-index: 100;
}

.login-container.right-panel-active .overlay-container{
	transform: translateX(-100%);
}

.overlay {
	background: #cc00ff;
	background-color: var(--color-five);
	background-repeat: no-repeat;
	background-size: cover;
	background-position: 0 0;
	color: #FFFFFF;
	position: relative;
	left: -100%;
	height: 100%;
	width: 200%;
  	transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}

.login-container.right-panel-active .overlay {
  	transform: translateX(50%);
}

.overlay-panel {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 40px;
	text-align: center;
	top: 0;
	height: 100%;
	width: 50%;
	transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}


.overlay-panel h1{
	position: relative;
	top: 50px;
}

.overlay-left {
	transform: translateX(-20%);
}

.login-container.right-panel-active .overlay-left {
	transform: translateX(0);
}

.overlay-right {
	right: 0;
	transform: translateX(0);
}

.login-container.right-panel-active .overlay-right {
	transform: translateX(20%);
}



.btn-login{
	width: 100%;
	padding: 10px 0;
	display: block;
	margin: 0 auto;
	border-radius: 10px;
	margin-top: 70px;
	background-color: transparent;
	color: var(--color-four);
	border: .5px solid var(--accent-color);
	transition: all .2s ease-out;
}

.btn-login:hover{
	background-color: var(--color-four);
	border: 1px solid var(--color-four);
	text-decoration: none;
	color: #fff;
}
.btn-login:active,
.btn-login:focus{
	outline: none;
}

.login-text{
	position: relative;
	text-align: center;
	top: 150px;
}


@media screen and (max-width: 600px) {
	.login-container {
		width: 80%;
		left: 10%;
	}

	.form-container {
		display: none;
	}

	.overlay-container{
		display: none;
	}

	.text h1{
		font-size: 32px;
	}
	
}

@media screen and (max-width: 820px) {
	p {
		font-size: 14px;
	}

	a {
		font-size: 10px;
		margin: 30px 0;
	}

	
	input {
		padding: 6px 8px;
		width: 200px;
		font-size: 12px;
	}

	.login-container {
        align-self: center;
		width: 80%;
		
	}

	.form-container {
		width: 30%;
		left: 10%;
	}


	.text h1{
		font-size: 20px;
		text-align: center;
	}

	.overlay-panel h1 {
		font-size: 24px;
		text-align: center;
	}
}
  #login {
    color: #bb00ff;
	text-align: center;
  }

  form {
	flex: 1 1 0%;
	padding: 8rem 1rem 1rem;
}

h1 {
	font-size: 40px;
	margin-bottom: 2rem;
	text-align: center;
}


input {
	appearance: none;
	border: none;
	outline: none;
	background: none;
	display: block;
	width: 100%;
	max-width: 400px;
	margin: 0 auto;
	font-size: 20px;;
	margin-bottom: 2rem;
	padding: 0.5rem 0rem;
}

input:not([type="submit"]) {
	opacity: 0.8;
	transition: 0.4s;
}
input:focus:not([type="submit"]) {
	opacity: 1;
}
input::placeholder {
	color: #dd77ff;
    height: 12;
}

  .card {
	min-height: 100vh;
    flex: 1 1 0%;
	padding: 8rem 1rem 1rem;
    background: #ffffff;
  }

  button:not([type="submit"]) {
	color: #cb83ff;
	border-bottom: 2px solid #e369ff;
}

  button[type="submit"] {
	background-color: rgb(183, 0, 255);
	color: #FFF;
	font-weight: 700;
	padding: 1rem 2rem;
	border-radius: 0.5rem;
	cursor: pointer;
} 

    label {
	color: rgb(0, 0, 0);
	font-weight: 700;
	padding: 1rem 2rem;
	border-radius: 0.5rem;
	cursor: pointer;
}

  </style>