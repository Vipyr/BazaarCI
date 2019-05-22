main()
function main() {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", "sample1.py", false);
  xmlhttp.overrideMimeType("text/plain")
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
    var sample1 = document.getElementById("Sample1")
    sample1.textContent = result
    sample1.className = "language-python"
  }

}
