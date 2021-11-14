<template>
  <div style="padding-top: 70px">
    <el-row
      type="flex"
      style="width: 100%"
      justify="center"
    >
      <el-col
        :xs="20"
        :sm="20"
        :md="16"
        :lg="10"
      >
        <el-form>
          <el-form-item>
            <el-input
              v-model="message"
              type="textarea"
              :rows="2"
              style="margin-bottom: 10px"
              placeholder="请输入弹幕内容"
            />
          </el-form-item>
          <el-form-item
            label="弹幕颜色"
            style="text-align:left"
          >
            <el-color-picker
              v-model="color"
              :predefine="['#409EFF','#67C23A','#E6A23C','#F56C6C','#909399','#303133']"
            />
          </el-form-item>
          <el-form-item>
            <el-button
              style="width: 100%"
              type="success"
              @click="sendBarrage"
            >
              Biu!
            </el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Sender',
  data() {
    return {
      message: '',
      author: '',
      color: '#409EFF',
    };
  },
  mounted() {
    this.author = this.$route.params.name;
  },
  methods: {
    sendBarrage() {
      const formData = new FormData();
      formData.append('message', this.message);
      formData.append('channel', this.author);
      formData.append('color', this.color);
      this.$axios.post('https://slides.magichc7.com/barrage-api/send', formData).then(() => {
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
