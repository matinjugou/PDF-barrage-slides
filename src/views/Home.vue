<template>
  <div
    style="position: relative;width: 100%;height: 100%;"
  >
    <div
      style="z-index: 1;position:absolute;width: 100%;top: 50%;
    left:50%;
    transform: translate(-50% , -50%);"
    >
      <pdf
        :src="url"
        :page="pageNum"
        @num-pages="numPages = $event"
      />
    </div>
    <vue-danmaku
      ref="danmaku"
      :danmus="arr"
      use-slot
      :speeds="170"
      :random-channel="true"
      style="z-index: 2;position:absolute;width: 100%;height:100%;"
    >
      <template
        slot="dm"
        slot-scope="{ danmuindex, danmu }"
      >
        <span
          :key="danmuindex"
          :style="`color: ${danmu.color};font-size: 30px`"
        >{{ danmu.message }}</span>
      </template>
    </vue-danmaku>
    <div style="z-index: 3;position:absolute;width: 100%;bottom: 20px">
      <span>当前演讲人是：{{ author }}，请访问：<a
        target="_blank"
        :href="`https://slides-cdn.magichc7.com/v3/#/sender/${author}`"
      >
        https://slides-cdn.magichc7.com/v3/#/sender/{{ author }}
      </a>发送弹幕
      </span>
    </div>
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
      author: '',
      url: '',
      pageNum: 1,
      numPages: 1,
      paused: false,
      arr: [],
      index: 0,
      timer: null,
    };
  },
  mounted() {
    this.author = this.$route.params.name;
    this.url = `https://slides-cdn.magichc7.com/v3/pdf/${this.author}.pdf`;
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
    this.timer = setInterval(this.playBarrage, 2000);
  },
  destroyed() {
    document.onkeydown = null;
    clearInterval(this.timer);
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
          channel: this.author,
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
      formData.append('channel', this.author);
      this.$axios.post('https://slides.magichc7.com/barrage-api/clean', formData).then(() => {
        this.message = '';
        this.$message({
          type: 'success',
          message: '弹幕已清空',
        });
        window.location.reload();
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
