document.addEventListener('DOMContentLoaded', function () {
  var form = document.querySelector('#upload_features'),
      btn = document.querySelector('.button'),
      loader = document.querySelector('.loader'),
      check = document.querySelector('.check');
  
  form.addEventListener('submit', function () {
    loader.classList.add('computing');    
  });
 
  loader.addEventListener('animationend', function() {
    check.classList.add('computing'); 
  });
});
