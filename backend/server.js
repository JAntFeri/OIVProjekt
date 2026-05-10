const express = require('express');
const cors = require('cors'); // npm install cors
const app = express();
const port = 3000;

// ========== SKRITI OSTANKI ==========
const r1 = "3660702654978408739515";
const r2 = "112638856742431508556";
const r3 = "3233313702270519969223";


app.use(cors({
    origin: '*', 
    exposedHeaders: ['X-Ref-A', 'X-Ref-B', 'X-Ref-C'] 
}));

app.get('/api/ui/theme-config', (req, res) => {
    res.set('Access-Control-Expose-Headers', 'X-Ref-A');
    res.set('X-Ref-A', r1);

    res.json({
        theme: "dark-industrial",
        version: "2.1.0",
        assets: ["/css/main.css", "/js/vendor.js"],
        primaryColor: "#00ff41"
    });
});

app.get('/api/ui/layout-manifest', (req, res) => {
    res.set('Access-Control-Expose-Headers', 'X-Ref-B');
    res.set('X-Ref-B', r2);

    res.json({
        grid: "bootstrap-5",
        breakpoints: { sm: 576, md: 768, lg: 992 },
        legacySupport: false
    });
});

app.get('/api/ui/font-loader', (req, res) => {
    res.set('Access-Control-Expose-Headers', 'X-Ref-C');
    res.set('X-Ref-C', r3);

    res.json({
        families: ["Syne", "DM Mono", "Lora"],
        weightRange: [400, 800],
        rendering: "antialiased"
    });
});

app.listen(port, () => {
    console.log(`UI Asset Server running on http://localhost:${port}`);
});