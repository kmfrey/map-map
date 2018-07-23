window.addEventListener('load', () => {
var basic = new Datamap({
  element: document.getElementById("basic"),
  responsive: true
});
window.addEventListener('resize', function() {
        basic.resize();
    });
});
