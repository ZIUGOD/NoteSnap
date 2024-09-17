function countCharactersAndWords(textarea) {
    const maxLength = 1024;
    const text = textarea.value;
    const charCount = text.length;
    const wordCount = text.trim().split(/\s+/).filter(Boolean).length;

    document.getElementById('charCount').innerText = `${charCount}/${maxLength} characters`;
    document.getElementById('wordCount').innerText = `${wordCount} words`;

    if (charCount >= maxLength) {
        textarea.value = text.substring(0, maxLength);
    }
}