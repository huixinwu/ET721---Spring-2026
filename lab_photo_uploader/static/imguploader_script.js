// Upload Image
document.querySelector('#uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const fileInput = document.querySelector('#imageInput');
    const message = document.querySelector('#message');

    if (!fileInput.files.length) {
        message.innerText = "Please select an image.";
        message.style.color = "red";
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            message.innerText = data.message;   // show server success message
            message.style.color = "green";

            // Optional: reload page after short delay
            setTimeout(() => {
                location.reload();
            }, 1000);

        } else {
            message.innerText = data.error || "Upload failed.";
            message.style.color = "red";
        }
    })
    .catch(error => {
        console.error('Error:', error);
        message.innerText = "Upload failed.";
        message.style.color = "red";
    });
});
// Delete Image
function deleteImage(id) {
    if (!confirm("Are you sure you want to delete this image?")) return;

    fetch(`/delete/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById(`image-${id}`).remove();
        } else {
            alert(data.error);
        }
    });
}