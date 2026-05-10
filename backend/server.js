const express = require('express');
const app = express();
const port = 3000;

const r1 = "3660702654978408739515"; 
const r2 = "112638856742431508556";
const r3 = "3233313702270519969223"; 

app.get('/api/validate', (req, res) => {
    res.set('Access-Control-Allow-Origin', '*'); // or '*' for testing
    res.set('Access-Control-Allow-Methods', 'GET');
    res.set('Access-Control-Allow-Headers', 'Content-Type');
    res.set('Access-Control-Expose-Headers', 'X-Ref-A, X-Ref-B, X-Ref-C');

    // 3. Set the custom headers
    res.set('X-Ref-A', r1);
    res.set('X-Ref-B', r2);
    res.set('X-Ref-C', r3);

    // 4. Send the "Decoy" body
    res.json({
        status: "success",
        message: "Server is healthy",
        timestamp: new Date().toISOString()
    });
});

app.listen(port, () => {
    console.log(`Backend active. Smuggling data on port ${port}`);
});