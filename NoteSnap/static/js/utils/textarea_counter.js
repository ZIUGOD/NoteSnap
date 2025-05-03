document.addEventListener('DOMContentLoaded', function() {
    const maxLength = 1024;
    const textarea = document.querySelector('textarea');
    const charCountElement = document.getElementById('charCount');
    const wordCountElement = document.getElementById('wordCount');

    function updateCounts() {
        const text = textarea.value;
        const charCount = text.length;
        const wordCount = text.trim().split(/\s+/).filter(Boolean).length;

        charCountElement.innerText = charCount ? `${charCount}/${maxLength} characters` : '';
        wordCountElement.innerText = wordCount ? `${wordCount} word${wordCount > 1 ? 's' : ''}` : '';

        if (charCount >= maxLength) {
            textarea.value = text.substring(0, maxLength);
        }
    }

    if (textarea) {
        textarea.addEventListener('input', updateCounts);
        updateCounts();
    }
});
