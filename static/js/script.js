function validateForm() {
    const name = document.getElementById('name').value.trim();
    const description = document.getElementById('description').value.trim();
    const price = document.getElementById('price').value.trim();
    const image_url = document.getElementById('image_url').value.trim();

    if (!name) {
        showError('Пожалуйста, введите название');
        return false;
    }

    if (!description) {
        showError('Пожалуйста, введите описание');
        return false;
    }

    if (!price || isNaN(parseFloat(price))) {
        showError('Пожалуйста, введите корректную цену');
        return false;
    }

    if (!image_url) {
        showError('Пожалуйста, введите URL изображения');
        return false;
    }

    return true;
}

function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    errorDiv.style.color = '#ff4444';
    errorDiv.style.margin = '10px 0';

    const form = document.querySelector('form');
    form.prepend(errorDiv);

    setTimeout(() => {
        errorDiv.remove();
    }, 3000);
}