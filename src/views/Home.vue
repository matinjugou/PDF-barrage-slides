<template>
  <div
    style="position: relative;width: 100%;height: 100%;"
  >
    <div style="z-index: 1;position:absolute;width: 100%;height: 100%;">
      <pdf
        :src="url"
        :page="pageNum"
        @num-pages="numPages = $event"
      />
    </div>
    <vue-danmaku
      ref="danmaku"
      :danmus="arr"
      :font-size="30"
      :speeds="170"
      :random-channel="true"
      extra-style="color: black"
      style="z-index: 2;position:absolute;width: 100%;height: 50%;top:20px"
    />
  </div>
</template>

<script>
import pdf from 'vue-pdf';
import vueDanmaku from 'vue-danmaku';

export default {
  name: 'Home',
  components: {
    pdf,
    vueDanmaku,
  },
  data() {
    return {
      url: './pdf/share.pdf',
      pageNum: 1,
      numPages: 1,
      paused: false,
      arr: [],
      index: 0,
    };
  },
  mounted() {
    document.onkeydown = (e) => {
      // 键盘按键判断:左箭头-37;上箭头-38；右箭头-39;下箭头-40
      if (e.code === 'ArrowLeft') {
        // 按下左箭头
        this.prePage();
      } else if (e.code === 'ArrowRight') {
        // 按下右箭头
        this.nextPage();
      } else if (e.code === 'KeyL') {
        // 按下L
        this.lastBarrage();
      } else if (e.code === 'KeyC') {
        // 按下C
        this.cleanBarrage();
      } else if (e.code === 'KeyP') {
        // 按下空格
        this.switchPause();
      } else if (e.code === 'KeyR') {
        // 按下R
        this.index = 0;
      }
    };
    setInterval(this.playBarrage, 2000);
  },
  methods: {
    prePage() {
      let page = this.pageNum;
      page = page > 1 ? page - 1 : 1;
      this.pageNum = page;
    },
    nextPage() {
      let page = this.pageNum;
      page = page < this.numPages ? page + 1 : this.numPages;
      this.pageNum = page;
    },
    lastBarrage() {
      for (let i = this.index - 5; i < this.index; i += 1) {
        if (i >= 0) {
          this.$refs.danmaku.push(this.arr[i]);
        }
      }
    },
    playBarrage() {
      this.$axios.get('https://slides.magichc7.com/barrage-api/get', {
        params: {
          channel: 'slides3',
          index: this.index,
        },
      }).then((res) => {
        res.data.forEach((item) => {
          this.$refs.danmaku.push(item);
          this.arr.push(item);
        });
        this.index += res.data.length;
      });
    },
    cleanBarrage() {
      const formData = new FormData();
      formData.append('channel', 'slides3');
      this.$axios.post('https://slides.magichc7.com/barrage-api/clean', formData).then(() => {
        this.message = '';
        this.$message({
          type: 'success',
          message: '弹幕已清空',
        });
        this.arr = [];
      });
    },
    switchPause() {
      if (this.paused) {
        this.paused = false;
        this.$refs.danmaku.play();
      } else {
        this.paused = true;
        this.$refs.danmaku.pause();
      }
    },
  },
};
</script>
