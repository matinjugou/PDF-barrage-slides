<template>
  <div style="width: 50%; margin:auto; padding-top: 70px">
    <el-input
      v-model="message"
      type="textarea"
      :rows="2"
      style="margin-bottom: 10px"
      placeholder="请输入弹幕内容"
    />
    <el-button
      style="width: 100%"
      type="success"
      @click="sendBarrage"
    >
      Biu!
    </el-button>
  </div>
</template>

<script>
export default {
  name: 'Sender',
  data() {
    return {
      message: '',
    };
  },
  methods: {
    sendBarrage() {
      const formData = new FormData();
      formData.append('message', this.message);
      formData.append('channel', 'slides3');
      this.$axios.post('http://127.0.0.1:5000/send', formData).then(() => {
        this.message = '';
        this.$message({
          type: 'success',
          message: '发送成功',
        });
      });
    },
  },
};
</script>
