<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hayyak – Dubai Relocation Guide</title>

    <!-- Google Fonts (Inter) -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap" rel="stylesheet" />

    <style>
        /* ---------- RESET & BASE ---------- */
        *,
        *::before,
        *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            padding: 32px 24px;
        }

        .app {
            max-width: 1440px;
            width: 100%;
            background: #ffffff;
            border-radius: 32px;
            box-shadow: 0 25px 60px -12px rgba(0, 0, 0, 0.15);
            display: grid;
            grid-template-columns: 300px 1fr;
            overflow: hidden;
            min-height: 860px;
        }

        /* ---------- SIDEBAR ---------- */
        .sidebar {
            background: #fafbfc;
            padding: 36px 24px 32px 28px;
            border-right: 1px solid #eef0f2;
            display: flex;
            flex-direction: column;
        }

        .sidebar-header {
            margin-bottom: 32px;
        }

        .sidebar-header .logo {
            font-size: 28px;
            font-weight: 800;
            letter-spacing: -0.5px;
            color: #0b1a33;
            line-height: 1.1;
        }

        .sidebar-header .logo span {
            color: #0066ff;
        }

        .sidebar-header .subtitle {
            font-size: 15px;
            font-weight: 500;
            color: #1f2a44;
            margin-top: 4px;
            letter-spacing: -0.2px;
        }

        .sidebar-header .journey-label {
            font-size: 13px;
            font-weight: 500;
            color: #6b7a93;
            margin-top: 12px;
            letter-spacing: 0.3px;
            text-transform: uppercase;
        }

        /* step list */
        .step-list {
            flex: 1;
            overflow-y: auto;
            margin-top: 4px;
            padding-right: 4px;
        }

        .step-list::-webkit-scrollbar {
            width: 4px;
        }
        .step-list::-webkit-scrollbar-track {
            background: #eef0f2;
            border-radius: 8px;
        }
        .step-list::-webkit-scrollbar-thumb {
            background: #c0c8d4;
            border-radius: 8px;
        }

        .step-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 12px 8px 8px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 500;
            color: #6b7a93;
            transition: background 0.15s, color 0.15s;
            cursor: default;
            margin-bottom: 2px;
        }

        .step-item .num {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 34px;
            height: 34px;
            border-radius: 10px;
            background: transparent;
            font-size: 13px;
            font-weight: 600;
            color: #6b7a93;
            transition: background 0.15s, color 0.15s;
            flex-shrink: 0;
        }

        .step-item .label {
            line-height: 1.3;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* active step */
        .step-item.active {
            background: #eef4ff;
            color: #0b1a33;
        }

        .step-item.active .num {
            background: #0066ff;
            color: #ffffff;
        }

        /* completed style (optional) */
        .step-item.completed .num {
            background: #e6edf5;
            color: #1f2a44;
        }

        /* ---------- MAIN CONTENT ---------- */
        .main {
            padding: 36px 44px 40px 40px;
            background: #ffffff;
        }

        /* breadcrumb / step badge */
        .step-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #eef4ff;
            color: #0066ff;
            font-size: 13px;
            font-weight: 600;
            padding: 6px 16px 6px 14px;
            border-radius: 40px;
            letter-spacing: 0.2px;
            margin-bottom: 16px;
        }

        .step-badge .dot {
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #0066ff;
            border-radius: 50%;
        }

        .main-title {
            font-size: 34px;
            font-weight: 700;
            color: #0b1a33;
            letter-spacing: -0.5px;
            line-height: 1.2;
            margin-bottom: 6px;
        }

        .main-sub {
            font-size: 17px;
            color: #4a5a72;
            font-weight: 400;
            margin-bottom: 24px;
            line-height: 1.5;
            max-width: 620px;
        }

        /* info chips */
        .info-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 24px 32px;
            background: #f8f9fb;
            padding: 16px 24px;
            border-radius: 16px;
            margin-bottom: 28px;
            border: 1px solid #eef0f2;
        }

        .chip {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            font-weight: 500;
            color: #1f2a44;
        }

        .chip .label {
            color: #6b7a93;
            font-weight: 400;
        }

        .chip .value {
            font-weight: 600;
            color: #0b1a33;
        }

        .chip .badge {
            background: #e6edf5;
            padding: 2px 12px;
            border-radius: 40px;
            font-size: 13px;
            font-weight: 500;
            color: #1f2a44;
        }

        /* section headings */
        .section-heading {
            font-size: 18px;
            font-weight: 600;
            color: #0b1a33;
            margin-bottom: 16px;
            margin-top: 28px;
        }

        .section-heading:first-of-type {
            margin-top: 0;
        }

        /* checklist */
        .checklist {
            list-style: none;
            padding: 0;
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 8px;
        }

        .checklist li {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 15px;
            color: #1f2a44;
            padding: 6px 12px 6px 8px;
            border-radius: 10px;
            transition: background 0.1s;
            line-height: 1.5;
        }

        .checklist li .check {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 22px;
            height: 22px;
            background: #eef4ff;
            border-radius: 6px;
            color: #0066ff;
            font-size: 14px;
            font-weight: 700;
            flex-shrink: 0;
            margin-top: 1px;
        }

        .checklist li .text {
            flex: 1;
        }

        /* important box */
        .important-box {
            background: #faf3e8;
            border-left: 4px solid #f5a623;
            padding: 18px 22px;
            border-radius: 12px;
            margin: 20px 0 24px 0;
        }

        .important-box .title {
            font-size: 14px;
            font-weight: 700;
            color: #8b6f3c;
            text-transform: uppercase;
            letter-spacing: 0.4px;
            margin-bottom: 8px;
        }

        .important-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .important-box ul li {
            font-size: 14px;
            color: #2d2a24;
            padding: 4px 0 4px 20px;
            position: relative;
            line-height: 1.6;
        }

        .important-box ul li::before {
            content: "•";
            position: absolute;
            left: 4px;
            color: #b8955a;
            font-weight: 700;
        }

        /* official links */
        .links-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 12px 24px;
            background: #f8f9fb;
            padding: 16px 20px;
            border-radius: 14px;
            border: 1px solid #eef0f2;
            margin-top: 4px;
        }

        .links-grid .link-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 14px;
            font-weight: 500;
            color: #0066ff;
            text-decoration: none;
        }

        .links-grid .link-item .domain {
            color: #1f2a44;
            font-weight: 400;
        }

        /* diagram / pro tip */
        .diagram-box {
            margin-top: 28px;
            background: #f2f6fe;
            border-radius: 16px;
            padding: 20px 24px;
            border: 1px solid #dfe8f5;
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        .diagram-box .icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            background: #0066ff;
            border-radius: 12px;
            color: #fff;
            font-size: 20px;
            font-weight: 700;
            flex-shrink: 0;
        }

        .diagram-box .content {
            flex: 1;
        }

        .diagram-box .content .label {
            font-size: 13px;
            font-weight: 600;
            color: #0066ff;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }

        .diagram-box .content .text {
            font-size: 15px;
            font-weight: 500;
            color: #0b1a33;
            margin-top: 2px;
        }

        /* ---------- RESPONSIVE ---------- */
        @media (max-width: 1024px) {
            .app {
                grid-template-columns: 260px 1fr;
            }
            .main {
                padding: 28px 28px 32px 28px;
            }
            .sidebar {
                padding: 28px 16px 24px 20px;
            }
        }

        @media (max-width: 768px) {
            .app {
                grid-template-columns: 1fr;
                border-radius: 24px;
            }
            .sidebar {
                border-right: none;
                border-bottom: 1px solid #eef0f2;
                padding: 20px 20px 12px 20px;
            }
            .sidebar-header .logo {
                font-size: 24px;
            }
            .step-list {
                display: flex;
                flex-wrap: nowrap;
                overflow-x: auto;
                gap: 4px;
                padding-bottom: 6px;
                margin-top: 8px;
            }
            .step-item {
                flex-shrink: 0;
                padding: 6px 12px 6px 8px;
                font-size: 13px;
                white-space: nowrap;
            }
            .step-item .label {
                white-space: nowrap;
            }
            .main {
                padding: 20px 20px 28px 20px;
            }
            .main-title {
                font-size: 26px;
            }
            .info-chips {
                flex-direction: column;
                gap: 10px;
                padding: 14px 18px;
            }
            .links-grid {
                flex-direction: column;
                gap: 8px;
            }
            .diagram-box {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        @media (max-width: 480px) {
            body {
                padding: 12px 8px;
            }
            .app {
                border-radius: 20px;
            }
            .main-title {
                font-size: 22px;
            }
            .step-badge {
                font-size: 12px;
                padding: 4px 12px 4px 10px;
            }
            .checklist li {
                font-size: 14px;
                padding: 4px 8px 4px 4px;
            }
        }
    </style>
</head>
<body>

    <div class="app">

        <!-- ===== SIDEBAR ===== -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="logo">Hay<span>yak</span></div>
                <div class="subtitle">Dubai Relocation Guide</div>
                <div class="journey-label">Step-by-step journey</div>
            </div>

            <nav class="step-list" role="navigation" aria-label="Relocation steps">
                <!-- 01 active -->
                <div class="step-item active">
                    <span class="num">01</span>
                    <span class="label">Visa &amp; Entry</span>
                </div>
                <div class="step-item">
                    <span class="num">02</span>
                    <span class="label">Medical Fitness</span>
                </div>
                <div class="step-item">
                    <span class="num">03</span>
                    <span class="label">Emirates ID</span>
                </div>
                <div class="step-item">
                    <span class="num">04</span>
                    <span class="label">Housing Search</span>
                </div>
                <div class="step-item">
                    <span class="num">05</span>
                    <span class="label">Property Check</span>
                </div>
                <div class="step-item">
                    <span class="num">06</span>
                    <span class="label">Tenancy Contract</span>
                </div>
                <div class="step-item">
                    <span class="num">07</span>
                    <span class="label">Ejari</span>
                </div>
                <div class="step-item">
                    <span class="num">08</span>
                    <span class="label">DEWA</span>
                </div>
                <div class="step-item">
                    <span class="num">09</span>
                    <span class="label">Move-in Permit</span>
                </div>
                <div class="step-item">
                    <span class="num">10</span>
                    <span class="label">Internet</span>
                </div>
                <div class="step-item">
                    <span class="num">11</span>
                    <span class="label">Mobile SIM</span>
                </div>
                <div class="step-item">
                    <span class="num">12</span>
                    <span class="label">Cooling / Chiller</span>
                </div>
                <div class="step-item">
                    <span class="num">13</span>
                    <span class="label">Handover</span>
                </div>
                <div class="step-item">
                    <span class="num">14</span>
                    <span class="label">Essentials</span>
                </div>
                <div class="step-item">
                    <span class="num">15</span>
                    <span class="label">Banking</span>
                </div>
                <div class="step-item">
                    <span class="num">16</span>
                    <span class="label">Healthcare</span>
                </div>
                <div class="step-item">
                    <span class="num">17</span>
                    <span class="label">Transport</span>
                </div>
                <div class="step-item">
                    <span class="num">18</span>
                    <span class="label">Docs Vault</span>
                </div>
                <div class="step-item">
                    <span class="num">19</span>
                    <span class="label">Hayyak Tip</span>
                </div>
            </nav>
        </aside>

        <!-- ===== MAIN CONTENT ===== -->
        <main class="main">

            <!-- step badge -->
            <div class="step-badge">
                <span class="dot"></span>
                STEP 01 OF 18
            </div>

            <!-- title -->
            <h1 class="main-title">Visa &amp; Entry Setup</h1>
            <p class="main-sub">
                Understand and complete your UAE entry and residency process.
            </p>

            <!-- info chips -->
            <div class="info-chips">
                <div class="chip">
                    <span class="label">⏱ Timeline</span>
                    <span class="value">1–3 weeks</span>
                </div>
                <div class="chip">
                    <span class="label">📄 Key Documents</span>
                    <span class="value">Passport, photos, employment/sponsorship docs</span>
                </div>
                <div class="chip">
                    <span class="label">⚡ Difficulty</span>
                    <span class="badge">Easy</span>
                </div>
            </div>

            <!-- What you need to do -->
            <h2 class="section-heading">What you need to do</h2>
            <ul class="checklist">
                <li>
                    <span class="check">✔</span>
                    <span class="text"><strong>Confirm your sponsorship type</strong><br />Check if your employer, family member, free zone, or yourself will sponsor the visa.</span>
                </li>
                <li>
                    <span class="check">✔</span>
                    <span class="text"><strong>Check your entry status</strong><br />Know whether you have an entry permit or are entering on a tourist/visit visa.</span>
                </li>
                <li>
                    <span class="check">✔</span>
                    <span class="text"><strong>Prepare required documents</strong><br />Passport copy, passport photos, employment or sponsorship documents.</span>
                </li>
                <li>
                    <span class="check">✔</span>
                    <span class="text"><strong>Apply for entry/residency</strong><br />Submit your application through the relevant UAE authority or sponsor.</span>
                </li>
                <li>
                    <span class="check">✔</span>
                    <span class="text"><strong>Track approval</strong><br />Monitor your application status until it is approved.</span>
                </li>
                <li>
                    <span class="check">✔</span>
                    <span class="text"><strong>Proceed to next steps</strong><br />Once approved, move to medical fitness and Emirates ID application.</span>
                </li>
            </ul>

            <!-- IMPORTANT TO KNOW -->
            <div class="important-box">
                <div class="title">⚠ IMPORTANT TO KNOW</div>
                <ul>
                    <li>Residency and identity services are handled through UAE authorities such as ICP, and sometimes GDRFA Dubai depending on your case.</li>
                    <li>Do not sign long-term commitments until you know when your residency process will be completed.</li>
                    <li>Requirements vary by visa type, sponsor, nationality, and free zone.</li>
                </ul>
            </div>

            <!-- OFFICIAL LINKS -->
            <h2 class="section-heading">OFFICIAL LINKS</h2>
            <div class="links-grid">
                <a href="#" class="link-item">
                    <span>🔗</span> ICP UAE Official Website <span class="domain">icp.gov.ae</span>
                </a>
                <a href="#" class="link-item">
                    <span>🔗</span> GDRFA Dubai <span class="domain">gdrfad.gov.ae</span>
                </a>
                <a href="#" class="link-item">
                    <span>🔗</span> UAE Gov Portal <span class="domain">u.ae</span>
                </a>
            </div>

            <!-- Diagram / Pro Tip -->
            <div class="diagram-box">
                <div class="icon">💡</div>
                <div class="content">
                    <div class="label">Pro Tip</div>
                    <div class="text">Start your visa process early to avoid delays in your move-in timeline.</div>
                </div>
            </div>

        </main>

    </div>

</body>
</html>