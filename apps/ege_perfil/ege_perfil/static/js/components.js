// Define a new component called button-counter
Vue.component('top-bar', {
  data: function () {
    return {
      count: 0,
      ege: ege
    }
  },
  template: '<div id="top-bar">\n' +
      '<div><span>Logo</span>\n' +
      '<span>Title</span>\n' +
      '<span>Search</span>\n' +
      '<span>Notification</span>\n' +
      '<span>Help</span>\n' +
      '<span>Message</span>\n' +
      '<span>${ege.user.presentation_name}</span></div>\n' +
      '<div>Breadcrumb</div>\n' +
      '  </div>'
});
