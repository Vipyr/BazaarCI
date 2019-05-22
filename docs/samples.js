const samples = [
  "SimpleGraph",
  "TwoProducts",
]


class PythonSample {
  constructor(samplename) {
    this.name = samplename
    this.filename = "samples/" + this.name + ".py"
  }

  addToDocument() {
    var div = document.createElement("div")
    var header = document.createElement("h3")
    var pre = document.createElement("pre")
    var code = document.createElement("code")
    document.body.append(div)
    div.append(header)
    div.append(pre)
    pre.append(code)
    header.textContent = this.name

    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", this.filename, false);
    xmlhttp.overrideMimeType("text/plain")
    xmlhttp.send();
    if (xmlhttp.status==200) {
      result = xmlhttp.responseText;
      code.textContent = result
      code.className = "language-python"
    }
    else {
      sample1.textContent = "Load of " + this.filename + " failed!"
    }
  }
}


main()

function main() {
  samples.forEach(function(samplename) {
    sample = new PythonSample(samplename)
    sample.addToDocument()
  })

}
