<template>
  <v-sheet>
    <v-overlay v-model="loadingProcess">
      <v-progress-circular :size="120" width="10" color="primary" indeterminate></v-progress-circular>
      <div
        style="color: #ffffff; font-size: 22px; margin-top: 20px; margin-left: -40px;"
      >Analyzing Your Video...</div>
    </v-overlay>
    <v-layout justify-center>
      <v-flex xs12 sm8 md6 lg4>
        <v-row justify="center" class="mx-0 mt-12">
          <div style="font-size: 34px; font-weight: 500; color: #343a40;">WELCOME</div>
        </v-row>
        <v-card elevation="0">
          <!-- 데스크톱 화면 설명 요약 -->
          <v-row justify="center" class="mx-0 mt-12" v-if="$vuetify.breakpoint.mdAndUp">
            <v-flex md7 class="mt-1">
              <div
                style="font-size: 20px; font-weight: 300; color: #888;"
              >This is Video auto tagging Service</div>
              <div
                style="font-size: 20px; font-weight: 300; color: #888;"
              >Designed for Youtube Videos</div>
              <div
                style="font-size: 20px; font-weight: 300; color: #888;"
              >It takes few minutes to analyze your Video!</div>
            </v-flex>
            <v-flex md5>
              <v-card width="240" elevation="0" class="ml-5">
                <v-img
                  width="240"
                  src="http://khuhub.khu.ac.kr/2020-1-capstone-design1/PKH_Project1/uploads/b70e4a173c2b7d5fa6ab73d48582dd6e/youtubelogoBlack.326653df.png"
                ></v-img>
              </v-card>
            </v-flex>
          </v-row>

          <!-- 모바일 화면 설명 요약 -->
          <v-card elevation="0" class="mt-8" v-else>
            <div
              style="font-size: 20px; font-weight: 300; color: #888; text-align: center"
            >This is Video auto tagging Service</div>
            <div
              style="font-size: 20px; font-weight: 300; color: #888; text-align: center"
            >Designed for Youtube Videos</div>
            <div
              style="font-size: 20px; font-weight: 300; color: #888; text-align: center"
            >It takes few minutes to analyze your Video!</div>
            <v-img
              style="margin: auto; margin-top: 20px"
              width="180"
              src="http://khuhub.khu.ac.kr/2020-1-capstone-design1/PKH_Project1/uploads/b70e4a173c2b7d5fa6ab73d48582dd6e/youtubelogoBlack.326653df.png"
            ></v-img>
          </v-card>

          <!-- Set Threshold -->
          <div
            class="mt-10"
            style="font-size: 24px; text-align: center; font-weight: 400; color: #5a5a5a;"
          >How To start this service</div>
          <div
            style="font-size: 20px; font-weight: 300; color: #888; text-align: center; margin-bottom: 15px"
          >
            <div>Set up Threshold of</div>
            <div>Recommended Youtube link</div>
          </div>
          <v-row style="max-width: 300px; margin: auto">
            <v-slider v-model="threshold" :thumb-size="20" thumb-label="always" :min="2" :max="15"></v-slider>
          </v-row>

          <!-- Upload Video -->
          <div
            style="font-size: 20px; font-weight: 300; color: #888; text-align: center"
          >Then, Just Upload your Video</div>
          <v-row justify="center" class="mx-0 mt-2">
            <v-card
              max-width="500"
              outlined
              height="120"
              class="pa-9"
              @dragover.prevent
              @dragenter.prevent
              @drop.prevent="onDrop"
            >
              <v-btn
                style="text-transform: none"
                @click="clickUploadButton"
                text
                large
                color="primary"
              >CLICK or DRAG & DROP</v-btn>
              <input ref="fileInput" style="display: none" type="file" @change="onFileChange" />
            </v-card>
          </v-row>

          <!-- 결과 화면 -->
          <div
            style="font-size: 24px; text-align: center; font-weight: 400; color: #5a5a5a;"
            class="mt-10"
          >The Results of Analyzed Video</div>
          <v-card outlined class="pa-2 mx-5 mt-6" elevation="0" min-height="67">
            <div
              style="margin-left: 5px; margin-top: -18px; background-color: #fff; width: 110px; text-align: center;font-size: 14px; color: #5a5a5a; font-weight: 500"
            >Generated Tags</div>
            <v-chip-group column>
              <v-chip color="secondary" v-for="(tag, index) in generatedTag" :key="index">{{ tag[0] }} : {{tag[1]}}</v-chip>
            </v-chip-group>
          </v-card>
          <v-card outlined class="pa-3 mx-5 mt-8" elevation="0" min-height="67">
            <div
              style="margin-left: 5px; margin-top: -22px; margin-bottom: 5px; background-color: #fff; width: 140px; text-align: center;font-size: 14px; color: #5a5a5a; font-weight: 500"
            >Related Youtube Link</div>
            <v-flex style="margin-bottom: 2px" v-for="(url) in YoutubeUrl" :key="url.id">
              <div>
                <a style="color: #343a40; font-size: 16px; font-weight: 500" :href="url">{{url}}</a>
              </div>
            </v-flex>
          </v-card>
          <div
            class="mt-3"
            style="font-size: 20px; font-weight: 300; color: #888; text-align: center"
          >If the Video is analyzed successfully,</div>
          <div
            class="mb-5"
            style="font-size: 20px; font-weight: 300; color: #888; text-align: center"
          >Result Show up in each of Boxes!</div>
        </v-card>

      </v-flex>
    </v-layout>
  </v-sheet>
</template>
<script>
export default {
  name: 'Home',
  data() {
    return {
      videoFile: '',
      YoutubeUrl: [],
      generatedTag: [],
      threshold: 5,
      successDialog: false,
      errorDialog: false,
      loadingProcess: false,
    };
  },
  created() {
    // this.YoutubeUrl = [];
    // this.generatedTag = [];
  },
  methods: {
    loadVideoInfo() {},
    uploadVideo(files) {
      this.loadingProcess = true;
      const formData = new FormData();
      formData.append('file', files[0]);
      formData.append('threshold', this.threshold);
      console.log(files[0]);
      this.$axios
        .post('/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((r) => {
          const tag = r.data.tag_result;
          const url = r.data.video_result;
          url.forEach((element) => {
            this.YoutubeUrl.push(element.video_url);
          });
          this.generatedTag = tag;
          this.loadingProcess = false;
          this.successDialog = true;
          console.log(tag, url);
        })
        .catch((e) => {
          this.errorDialog = true;
          console.log(e.message);
        });
    },
    onDrop(event) {
      this.uploadVideo(event.dataTransfer.files);
    },
    clickUploadButton() {
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      this.uploadVideo(event.target.files);
    },
  },
};
</script>
