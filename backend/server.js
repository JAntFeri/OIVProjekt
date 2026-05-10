const express = require('express');
const app = express();
const port = 3000;

// ========== SKRITI OSTANKI ==========
const r1 = "3660702654978408739515";
const r2 = "112638856742431508556";
const r3 = "3233313702270519969223";

// ==================== ENDPOINTI ====================

// Endpoint 1 - izgleda kot normalen status check
app.get('/api/status/1', (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Expose-Headers', 'X-Ref-A');
    res.set('X-Ref-A', r1);

    res.json({
        status: "ok",
        message: "Server is healthy",
        timestamp: new Date().toISOString(),
        uptime: "99.87%",
        load: "12%"
    });
});

// Endpoint 2
app.get('/api/status/2', (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Expose-Headers', 'X-Ref-B');
    res.set('X-Ref-B', r2);

    res.json({
        status: "ok",
        message: "Server is healthy",
        timestamp: new Date().toISOString(),
        version: "1.4.2",
        activeUsers: 1247
    });
});

// Endpoint 3
app.get('/api/status/3', (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Expose-Headers', 'X-Ref-C');
    res.set('X-Ref-C', r3);

    res.json({
        status: "ok",
        message: "Server is healthy",
        timestamp: new Date().toISOString(),
        database: "connected",
        responseTime: "23ms"
    });
});

// Optional: Vsi naenkrat (za hitro testiranje)
app.get('/api/status', (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Expose-Headers', 'X-Ref-A, X-Ref-B, X-Ref-C');
    res.set('X-Ref-A', r1);
    res.set('X-Ref-B', r2);
    res.set('X-Ref-C', r3);

    res.json({
        status: "ok",
        message: "All systems operational",
        timestamp: new Date().toISOString()
    });
});

app.listen(port, () => {
    console.log(`Steganography server running on http://localhost:${port}`);
});