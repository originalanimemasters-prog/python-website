// JavaScript runner
const fs = require('fs');

let code = '';
process.stdin.on('data', chunk => {
    code += chunk.toString();
});

process.stdin.on('end', () => {
    fs.writeFileSync('solution.js', code);
    
    const { execSync } = require('child_process');
    
    try {
        const output = execSync('node solution.js', {
            timeout: 5000,
            encoding: 'utf-8'
        });
        console.log(JSON.stringify({
            stdout: output,
            stderr: '',
            exit_code: 0
        }));
    } catch (error) {
        console.log(JSON.stringify({
            stdout: error.stdout || '',
            stderr: error.stderr || error.message,
            exit_code: error.status || -1
        }));
    }
});
