var appVersion = new Vue({
  el: '#vjs-version',
  data: {
    currentVersion: '...',
    versions: [],
  },
  methods: {
    onVersion: function (data) {
      // Update the current version from received data
      this.currentVersion = data.version;
    },
    onVersions: function (data) {
      // Update version list from received data
      this.versions = data.versions;
    },
  },
  created: function () {
      // Call the server to obtain the version and others
      Promise.all([
        axios.get('version.json'),
        axios.get('../versions.json'),
      ]).then((datas) => {
        this.onVersion(datas[0].data);
        this.onVersions(datas[1].data);
      });
  },
  delimiters: ['((', '))']
});
