<template>
  <v-app>
    <v-app-bar app color="#ffffff" elevation="1" hide-on-scroll>
      <v-icon size="35" class="mr-1" color="grey700">mdi-youtube</v-icon>
      <div style="color: #343a40; font-size: 20px; font-weight: 500;">Youtube Auto Tagger</div>
      <v-spacer></v-spacer>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on" color="grey700" @click="clickInfo=true">
            <v-icon size="30">mdi-information</v-icon>
          </v-btn>
        </template>
        <span>Service Info</span>
      </v-tooltip>
    </v-app-bar>
    <v-dialog v-model="clickInfo" max-width="600" class="pa-2">
      <v-card elevation="0" outlined class="pa-4">
        <v-row justify="center" class="mx-0 mb-8 mt-2">
          <v-icon color="primary">mdi-power-on</v-icon>
          <div
            style="text-align: center; font-size: 22px; font-weight: 400; color: #343a40;"
          >Information of This Service</div>
          <v-icon color="primary">mdi-power-on</v-icon>
        </v-row>
        <v-btn color="primary" class="mt-2" block>Description of service</v-btn>
        <v-btn color="primary" class="my-2" block>Term of this service</v-btn>
        <v-btn color="primary" block>Used Opensource</v-btn>
      </v-card>
    </v-dialog>
    <v-content>
      <router-view />
    </v-content>
    <v-footer>
      <v-row justify="center">
        <v-avatar size="25" tile style="border-radius: 4px">
          <v-img src="http://khuhub.khu.ac.kr/2020-1-capstone-design1/PKH_Project1/uploads/99f7d5c73e506d2c5c0072a21f362181/logo.69342704.png"></v-img>
        </v-avatar>
        <a href="http://khuhub.khu.ac.kr/2020-1-capstone-design1/PKH_Project1">
          <div
            style="margin-left: 4px; font-size: 16px; color: #5a5a5a; font-weight: 400"
          >Profit-Hunter</div>
        </a>
      </v-row>
    </v-footer>
  </v-app>
</template>
<script>
export default {
  name: 'App',
  data() {
    return {
      clickInfo: false,
    };
  },
};
</script>
<style lang="scss">
a:hover {
  text-decoration: none;
}
a:link {
  text-decoration: none;
}
a:visited {
  text-decoration: none;
}
</style>
