import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
	let disposable = vscode.commands.registerCommand('extension.removePythonComments', () => {
		const editor = vscode.window.activeTextEditor;

		if (!editor) {
			vscode.window.showErrorMessage('Dont active editor.');
			return;
		}

		const document = editor.document;
		if (document.languageId !== 'python') {
			vscode.window.showWarningMessage('Recomend File Sintack (.py).');
		}
		const regex = /(^[ \t]*#.*(?:\r?\n|$))|("""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|([ \t]*#.*$)/gm;

		const selections = editor.selections;
		const hasSelection = selections.some(selection => !selection.isEmpty);

		editor.edit(editBuilder => {
			if (hasSelection) {
				selections.forEach(selection => {
					if (selection.isEmpty) { return; }

					const text = document.getText(selection);
					const newText = processText(text, regex);
					editBuilder.replace(selection, newText);
				});
			} else {
				// Hapus komentar di SELURUH dokumen
				const fullText = document.getText();
				const newText = processText(fullText, regex);

				const fullRange = new vscode.Range(
					document.positionAt(0),
					document.positionAt(fullText.length)
				);
				editBuilder.replace(fullRange, newText);
			}
		}).then(success => {
			if (success) {
				vscode.window.showInformationMessage('Comment Python Removed Successfuly !');
			}
		});
	});

	context.subscriptions.push(disposable);
}

function processText(text: string, regex: RegExp): string {
	return text.replace(regex, (match, fullLineComment, stringLiteral, inlineComment) => {
		if (stringLiteral) {
			return stringLiteral;
		}

		return '';
	});
}

export function deactivate() { }