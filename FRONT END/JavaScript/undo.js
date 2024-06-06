// undo.js
window.addEventListener('DOMContentLoaded', function() {
  document.getElementById('undo-button').addEventListener('click', function(event) {
    // 模拟 Ctrl+Z 快捷键
    var ctrlZEvent = new KeyboardEvent('keydown', {
      bubbles: true,
      cancelable: true,
      key: 'z',
      code: 'KeyZ',
      keyCode: 90,
      which: 90,
      ctrlKey: true
    });
    console.log('Button clicked!');
    document.dispatchEvent(ctrlZEvent);
  });
});