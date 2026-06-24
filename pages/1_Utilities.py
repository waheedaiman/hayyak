import streamlit as st

from src.ui import apply_hayyak_theme, arabic_divider, render_nav


st.set_page_config(
    page_title="Hayyak | Utilities",
    page_icon="🔌",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="utilities")


UTILITIES = {
    "DEWA": {
        "icon": "D",
        "description": "Electricity and water activation for your Dubai home.",
        "steps": """
### What this is

DEWA is Dubai Electricity and Water Authority. You usually need DEWA when moving into a rented apartment or villa so electricity and water are activated under your tenancy.

### Before you start

Prepare:

- Signed tenancy contract.
- Ejari registration or tenancy registration process.
- DEWA premise number, usually found on the property door or given by the landlord, agent, or building management.
- Emirates ID if available.
- Passport and visa details if requested.
- Payment method for deposit and activation charges.

### Step-by-step guide

1. **Confirm the property details**
   Check the unit number, building name, and DEWA premise number. Do not guess this number because using the wrong premise number can delay activation.

2. **Complete or start Ejari**
   DEWA activation is closely connected with tenancy registration. In many rental flows, DEWA move-in is linked to Ejari.

3. **Open the official DEWA Move-In service**
   Use the official DEWA Move-In page and enter the requested tenancy/property details.

4. **Review all account details**
   Check tenant name, premise number, unit details, and contact information before submitting.

5. **Pay the required deposit and charges**
   Pay only through official DEWA channels. Save the payment receipt.

6. **Wait for activation**
   DEWA says that if supply is not activated within 15 working hours after security deposit payment, users should contact DEWA Customer Care.

7. **Save your DEWA account details**
   Keep your DEWA account number, receipts, and confirmation emails because you may need them later for billing, move-out, or deposit refund.

### Common mistakes

- Applying with the wrong premise number.
- Waiting until move-in day.
- Assuming the landlord has already activated electricity and water.
- Losing payment confirmation.
- Trusting unofficial fee information.

### Official links

- [DEWA Move-In service](https://dewa.gov.ae/en/consumer/supply-management/activation-of-electricity-water-move-in)
- [DEWA official website](https://www.dewa.gov.ae/)
""",
    },
    "Ejari": {
        "icon": "E",
        "description": "Register your tenancy contract through Dubai Land Department systems.",
        "steps": """
### What this is

Ejari is Dubai’s tenancy contract registration system. It formally registers your rental contract and is often needed for DEWA, housing documentation, and other move-in processes.

### Before you start

Prepare:

- Signed tenancy contract.
- Tenant Emirates ID if available.
- Tenant passport and visa details if requested.
- Landlord details.
- Property/title deed details if requested.
- Payment method.
- Access to Dubai REST, Ejari system, property management company, or authorised service centre.

### Step-by-step guide

1. **Sign the tenancy contract**
   Check that the names, rent amount, unit number, and contract dates are correct.

2. **Choose your registration route**
   Dubai Land Department lists registration through channels such as service centres, property management companies, Ejari system, or Dubai REST.

3. **Submit the required documents**
   Upload or submit the tenancy contract and requested identity/property documents.

4. **Pay the official service fees**
   Use the amount shown by the official channel during registration.

5. **Wait for approval**
   Once approved, the e-contract registration certificate is issued.

6. **Download and save your Ejari certificate**
   Keep it in your relocation folder. You may need it for DEWA, telecom setup, bank address updates, or other services.

### Common mistakes

- Submitting a contract with incorrect unit details.
- Uploading unclear scans.
- Assuming Ejari is optional.
- Waiting until another service asks for it.
- Not saving the final certificate.

### Official links

- [Dubai Land Department - Register / Renew Ejari Contract](https://dubailand.gov.ae/en/eservices/register-renew-ejari-contract/)
- [Dubai Land Department official website](https://dubailand.gov.ae/)
""",
    },
    "e& Home Internet": {
        "icon": "e&",
        "description": "Set up or move e& home internet for your Dubai property.",
        "steps": """
### What this is

e& provides home internet, TV, and landline packages in the UAE. Newcomers may need a new home connection, while existing customers may need to move an eLife plan to a new address.

### Before you start

Prepare:

- New home address and unit details.
- Building/community name.
- Tenancy contract or proof of residence if requested.
- Emirates ID if available.
- Current e& account details if moving an existing service.
- Preferred installation date and time.
- Router/equipment details if you already have e& service.

### Step-by-step guide

1. **Check building availability**
   Confirm whether e& service is available in your building.

2. **Choose new setup or home move**
   If you already have e&, use the Home Move flow. If you are new, compare home internet packages first.

3. **Use official e& channels**
   e& describes the Home Move flow through the e& UAE app: go to the eLife Plan tab, tap Manage, then Home Move.

4. **Enter the new address carefully**
   Add exact building, unit, and area details.

5. **Upload documents if requested**
   Submit tenancy contract, Emirates ID, or proof of residence if required.

6. **Book installation**
   Choose a technician visit slot and make sure someone can access the apartment.

7. **Test the connection**
   Test Wi-Fi speed in multiple rooms after installation.

### Common mistakes

- Booking before confirming building coverage.
- Not being available for the technician.
- Forgetting existing router/equipment.
- Ignoring contract terms or relocation fees.
- Not testing Wi-Fi after installation.

### Official links

- [e& Home Move](https://www.eand.ae/en/c/home/home-moving.html)
- [e& UAE official website](https://www.eand.ae/)
""",
    },
    "du Home Internet": {
        "icon": "du",
        "description": "Set up or relocate du home internet, TV, and landline services.",
        "steps": """
### What this is

du provides home internet, TV, and landline services in the UAE. Existing du Home users can request home relocation online.

### Before you start

Prepare:

- New address and unit number.
- Building/community name.
- Tenancy contract or title deed.
- Proof of relationship if the tenancy is not in your name.
- Emirates ID if available.
- Current du account details if relocating.
- Preferred installation date and time.

### Step-by-step guide

1. **Check if du is available in your building**
   Ask building management or check through du’s official channels.

2. **Open the official du relocation page**
   Start the home relocation request online.

3. **Upload required documents**
   du says users may need tenancy contract or title deed. If the tenancy is not under your name, proof of relationship may be required.

4. **Review the relocation fee**
   du states that a moving fee of AED 100 will be added to the next bill. Confirm the final amount during the official request.

5. **Schedule installation**
   Choose a technician appointment and make sure access is available.

6. **Prepare your devices**
   Keep router, TV box, landline device, remotes, cables, and power adapters ready.

7. **Test after setup**
   Test Wi-Fi, TV, and landline if included.

### Common mistakes

- Assuming both du and e& are available in every building.
- Missing the technician appointment.
- Uploading incomplete documents.
- Forgetting contract terms.
- Not testing connection quality after setup.

### Official links

- [du Home relocation](https://www.du.ae/personal/at-home/moving-to-a-new-home)
- [du official website](https://www.du.ae/)
""",
    },
    "Mobile SIM / eSIM": {
        "icon": "SIM",
        "description": "Get connected with UAE mobile service through du or e&.",
        "steps": """
### What this is

Newcomers usually need a UAE mobile number soon after arrival. Visitors can start with tourist SIM/eSIM options. Residents can later move to prepaid or postpaid plans using Emirates ID.

### Before you start

Prepare:

- Passport if you are a visitor.
- Emirates ID if you are a UAE resident.
- UAE PASS access if using digital verification.
- eSIM-compatible phone if choosing eSIM.
- Unlocked phone that supports UAE networks.
- Payment method.

### Step-by-step guide for visitors

1. **Choose tourist SIM or eSIM**
   e& and du offer visitor/tourist mobile plans.

2. **Register with passport details**
   Use your official passport details.

3. **Activate the line**
   Follow the provider’s activation process. For eSIM, confirm that your phone supports eSIM and is not carrier locked.

4. **Choose the data package**
   Pick based on maps, WhatsApp, delivery apps, hotspot needs, and stay length.

5. **Track validity**
   Tourist SIMs usually have limited validity, so set a reminder before expiry.

### Step-by-step guide for residents

1. **Prepare Emirates ID**
   Emirates ID is required for resident telecom registration.

2. **Choose prepaid or postpaid**
   Prepaid is usually easier early on. Postpaid can make sense after residency and income details are stable.

3. **Register the number**
   Use the provider app, website, or store.

4. **Keep registration updated**
   Providers require valid identity registration. Update Emirates ID details when renewed.

5. **Track usage**
   Download the provider app and monitor data, renewal, and add-ons.

### Common mistakes

- Buying a plan before checking phone compatibility.
- Forgetting tourist SIM expiry.
- Not updating Emirates ID.
- Ignoring auto-renewal.
- Buying from unofficial sellers.

### Official links

- [TDRA Mobile Consumer Registration](https://tdra.gov.ae/en/initiatives/registration-for-mobile-consumers)
- [e& Visitor Line](https://www.eand.ae/en/c/mobile/plans/visitor-line.html)
- [du Tourist SIM](https://shop.du.ae/en/personal/prepaid/du-tourist-prepaid-plans?view=bundles)
- [e& Mobile Registration Renewal](https://www.eand.ae/en/c/mobile-registration-renewal.html)
- [du Emirates ID update](https://www.du.ae/support/id-renewal)
""",
    },
    "UAE PASS": {
        "icon": "ID",
        "description": "Set up UAE digital identity access for supported services.",
        "steps": """
### What this is

UAE PASS is the UAE’s national digital identity platform. It helps users access many government and partner services online.

### Before you start

Prepare:

- Smartphone.
- UAE mobile number.
- Emirates ID if you are a resident.
- Passport/visitor details if supported.
- UAE PASS app.
- Secure PIN and access to OTPs.

### Step-by-step guide

1. **Download the official UAE PASS app**
   Use the official app store listing.

2. **Register your account**
   Enter your personal details and mobile number.

3. **Verify your identity**
   Follow the official verification steps in the app.

4. **Set up security**
   Create a PIN and use biometrics if available.

5. **Use UAE PASS for supported services**
   Use it to log in to supported UAE government and partner portals.

### Common mistakes

- Using someone else’s phone number.
- Sharing OTPs or PINs.
- Expecting full access without verification.
- Using UAE PASS on a shared phone.
- Signing documents without reading them.

### Official links

- [UAE PASS official website](https://uaepass.ae/)
- [UAE Government - Emirates ID](https://u.ae/en/information-and-services/visa-and-emirates-id/emirates-id)
""",
    },
}


@st.dialog("Utility setup guide")
def show_utility_modal(name, item):
    st.subheader(name)
    st.caption(item["description"])
    arabic_divider()

    st.markdown(item["steps"])

    st.divider()
    st.caption(
        "Hayyak note: official processes, fees, required documents, and timelines can change. "
        "Always confirm details through the linked official service before applying."
    )


st.markdown(
    """
    <section class="hero-shell">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">Move-in setup</div>
                <h1 class="hero-title">Utilities</h1>
                <p class="hero-copy">
                    A calm, structured place to understand the essential services
                    newcomers usually need when settling into a Dubai home.
                </p>
            </div>
            <div class="brand-card">
                <h3 style="color:#642A16;margin-bottom:.5rem;">Setup without the overwhelm</h3>
                <p class="muted-text">
                    Each card opens a focused guide instead of forcing users
                    through a long page of information.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="section-card">
        <div class="section-heading">
            <div>
                <h2>Choose a setup area</h2>
                <p>Select a utility to view its move-in checklist.</p>
            </div>
        </div>
    """,
    unsafe_allow_html=True,
)


items = list(UTILITIES.items())
cols = st.columns(3)

for index, (name, item) in enumerate(items):
    with cols[index % 3]:
        st.markdown(
            f"""
            <div class="utility-card">
                <div class="utility-icon">{item["icon"]}</div>
                <h3 style="margin:.2rem 0;color:#642A16;">{name}</h3>
                <p class="muted-text">{item["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(f"View {name} steps", key=f"utility_{name}"):
            show_utility_modal(name, item)

st.markdown("</div>", unsafe_allow_html=True)
