var editor = CodeMirror.fromTextArea
        (document.getElementById('editor'), {
            //mode: 'xml',
            mode: 'text/x-python',
            theme: 'dracula',
            lineNumbers: true,
            lineSeparator: '  ',
            autofocus: true,
            
        })
editor.setSize('800', '300')