window.onload = function() {
  var fileInput = document.getElementById("image-flower");
  var fileInputLabel = document.getElementById("image-label");
  console.log(fileInputLabel);
  console.log(fileInput)

  fileInput.addEventListener("change", () => {
    const fileName = fileInput.value.split("\\").pop();
    fileInputLabel.innerHTML = fileName;
  });
};
