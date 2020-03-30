module.exports = {
  devServer: {
    proxy: {
      '/*': {
        target: "http://192.168.5.87:5000/",
        logLevel: 'debug'
      }
    }
  }
}
