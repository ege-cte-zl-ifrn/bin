<template>
  <v-app id="inspire">
    <v-content style="padding:0">
      <v-container fluid fill-height style="padding:0">
        <v-layout align-center justify-center column>
          <v-flex d-flex align-center style="flex-direction:column">
            <img
              :src="photo_user"
              class="elevation-6"
              style="z-index:1; position:relative; width: 15%; top: 5em; border-radius:50%; flex:0 !important"
            >
            <v-card class="elevation-12" style="max-width:85%;width:50em;border-top:2px solid LightGray">
              <v-card-title primary-title class="mt-5">
                <div style="width:100%">
                  <h3 dark class="headline mb-0 mt-3">Nome do aluno</h3>
                  <div class="d-flex row align-center justify-between mt-3">
                    <div>
                      <h5>Matrícula</h5>
                      <p>0000.0000.000-00</p>
                    </div>
                    <div>
                      <h5>Pólo</h5>
                      <p>Apodi</p>
                    </div>
                    <div>
                      <h5>Campus</h5>
                      <p>EAD</p>
                    </div>
                  </div>
                </div>

                <v-divider style="margin:0 25px"></v-divider>

                <div style="width:100%">
                  <div class="d-flex row align-center justify-between mt-3">
                    <div>
                      <h5>Biografia</h5>
                      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque blandit arcu eget consectetur fringilla. Suspendisse potenti. Ut egestas interdum efficitur. Quisque varius tempus dapibus. Quisque iaculis, sapien et condimentum semper, nibh ligula vehicula dolor, nec dapibus ligula ex id libero. Maecenas pulvinar tortor eu suscipit vestibulum. Quisque tristique quis elit a posuere. Sed ac sem mollis, laoreet mi a, pulvinar tellus. Aenean at eros augue. Duis sed lacus quam. Sed dignissim, arcu at laoreet elementum, leo lorem interdum urna, vel laoreet sem orci a diam. Phasellus a nulla a turpis eleifend elementum vel non metus. Aliquam interdum molestie dapibus. Morbi laoreet augue nibh, non venenatis libero tincidunt vel. Donec posuere tortor a ligula consectetur, ut eleifend est scelerisque.</p>
                    </div>
                  </div>
                </div>

                <v-divider style="margin:0 25px"></v-divider>

                <div style="width:100%">
                  <div class="d-flex row align-center justify-between mt-3">
                    <div>
                      <h5>E-mail</h5>
                      <p class="mt-2">email@email.com</p>
                    </div>
                  </div>
                </div>
                
                <v-divider style="margin:0 25px"></v-divider>

                <div style="width:100%">
                  <div class="d-flex row align-center justify-between mt-3">
                    <div>
                      <h5>Recurso de acessibilidade</h5>
                      <div style="line-height:1em">
                        <p class="mb-0 mt-2">Libras</p>
                        <p style="color:grey">Ativado</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <v-divider style="margin:0 25px"></v-divider>

                <div style="width:100%">
                  <div class="d-flex row align-center justify-between mt-3">
                    <div>
                      <h5>Necessidades especiais</h5>
                      <p class="mt-2">Baixa visão</p>
                    </div>
                  </div>
                </div>
                
                <v-divider style="margin:0 25px"></v-divider>

                <div style="width:100%">
                  <div class="d-flex row align-center justify-between mt-3">
                    <div>
                      <h5>Cursos inscritos</h5>
                      <v-card class="mt-2">
                        <v-card-title>
                          <div style="width:100%">
                            <p dark>Tecnologia e Desenvolvimento de Software</p>
                            <div class="d-flex row align-center justify-between">
                              <div>
                                <span style="color:grey">0000.0000.000-00</span>
                              </div>
                              <div>
                                <span style="color:grey">Média Final: 9.0</span>
                              </div>
                            </div>
                            <v-progress-linear
                              v-model="valueDeterminate_1"
                              color="success"
                            ></v-progress-linear>
                          </div>
                        </v-card-title>
                      </v-card>

                      <v-card class="mt-2">
                        <v-card-title>
                          <div style="width:100%">
                            <p dark>Gestão Ambiental</p>
                            <div class="d-flex row align-center justify-between">
                              <div>
                                <span style="color:grey">0000.0000.000-00</span>
                              </div>
                            </div>
                            <v-progress-linear
                              v-model="valueDeterminate_2"
                              color="warning"
                            ></v-progress-linear>
                          </div>
                        </v-card-title>
                      </v-card>
                    </div>
                  </div>
                </div>
              </v-card-title>
            </v-card>
          </v-flex>
          
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        card_text: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.',
        photo_user: 'https://cdn3.iconfinder.com/data/icons/black-easy/512/538642-user_512x512.png',
        valueDeterminate_1: 100,
        valueDeterminate_2: 30
      }
    }
  }
</script>