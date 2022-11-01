<template>
  <nav>
    <router-link to="/Inicio"> | Inicio | </router-link>
    <router-link to="/Docente"> | Docente | </router-link>
    <router-link to="/Coordinador"> | Coordinador | </router-link>
  </nav>
  <div id="app">
    <router-view />
  </div>

</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #9d00ff;
}

nav {
  padding: 30px;
  background: #722bff;
}

nav a {
  font-weight: bold;
  color: #ffffff;
}

nav a.router-link-exact-active {
  color: #b3f7ff;
}

</style>
