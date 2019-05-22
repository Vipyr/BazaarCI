main()
function main() {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", "simple_graph.py", false);
  xmlhttp.overrideMimeType("text/plain")
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
    var sample1 = document.getElementById("SimpleGraph")
    sample1.textContent = result
    sample1.className = "language-python"
  }

}
