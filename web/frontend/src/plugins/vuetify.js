import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#343a40',
        secondary: '#506980',
        accent: '#505B80',
        error: '#FF5252',
        info: '#2196F3',
        blue: '#173f5f',
        lightblue: '#72b1e4',
        success: '#2779bd',
        warning: '#12283a',
        grey300: '#eceeef',
        grey500: '#aaaaaa',
        grey700: '#5a5a5a',
        grey900: '#212529',
      },
      dark: {
        primary: '#343a40',
        secondary: '#506980',
        accent: '#505B80',
        error: '#FF5252',
        info: '#2196F3',
        blue: '#173f5f',
        lightblue: '#72b1e4',
        success: '#2779bd',
        warning: '#12283a',
        grey300: '#eceeef',
        grey500: '#aaaaaa',
        grey700: '#5a5a5a',
        grey900: '#212529',
      },
    },
  },
});
