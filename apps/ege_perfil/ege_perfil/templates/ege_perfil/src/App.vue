<template>
  <v-app>
    <v-toolbar app color="#5AC26C">
      <img :src="logo" class="mr-5" style="width:10%">
      <v-divider vertical dark style="border-width:thin"></v-divider>
      <h2 class="ml-3" style="color:white">Perfil</h2>
      <v-spacer></v-spacer>
      <v-text-field
        class="mt-2"
        flat
        label="Pesquisar"
        prepend-inner-icon="search"
        solo-inverted
        style="width:1em"
      ></v-text-field>
      <div style="width:12em;display:flex;flex-direction:row;justify-content:space-around">
        <v-icon color="white darken-2">notifications</v-icon>
        <v-icon color="white darken-2">help</v-icon>
        <v-icon color="white darken-2">chat</v-icon>
      </div>
      <div style="width:14em;display:flex;flex-direction:row;justify-content:space-around;align-items:center">
        <img :src="photo_user" style="width:4em;height:4em;border-radius:50%;">
        <div style="line-height:1em">
          <h3 style="color:white">Primeiro Nome</h3>
          <span style="color:#006400">Aluno</span>
        </div>
      </div>
    </v-toolbar>

    <v-content>
      <ProfileCard/>
    </v-content>
  </v-app>
</template>

<script>
import ProfileCard from './components/ProfileCard'

export default {
  name: 'App',
  components: {
    ProfileCard
  },
  data () {
    return {
      logo: 'ege.svg',
      photo_user: 'https://cdn3.iconfinder.com/data/icons/black-easy/512/538642-user_512x512.png'
    }
  }
}
</script>
