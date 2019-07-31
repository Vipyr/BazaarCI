const samples = [
  "SimpleGraph",
  "TwoProducts",
]


function code_sample(samplename) {
  var filename = "samples/" + samplename + ".py"
  var div = document.createElement("div")

  var header = document.createElement("h3")
  header.textContent = samplename

  var pre = document.createElement("pre")
  pre.setAttribute("data-type", "text/plain")
  pre.setAttribute("data-src", filename)

  div.append(header)
  div.append(pre)
  return div
}


function main() {
  samples.forEach(function(samplename) {
    document.getElementById("Samples").append(code_sample(samplename))
  })
  console.log(document)

}


main()
