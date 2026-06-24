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
        "subtitle": "Electricity and water activation",
        "description": (
            "Set up electricity and water for your Dubai home after your tenancy details "
            "are ready."
        ),
        "official_links": [
            ("DEWA Move-In service", "https://dewa.gov.ae/en/consumer/supply-management/activation-of-electricity-water-move-in"),
            ("DEWA homepage", "https://www.dewa.gov.ae/"),
        ],
        "content": """
### What this is

DEWA is Dubai Electricity and Water Authority. You normally deal with DEWA when moving into a rented apartment or villa so that electricity and water are activated under your tenancy.

### Before you start

Prepare or confirm:

- Your signed tenancy contract.
- Your Ejari registration or tenancy registration process.
- Your 9-digit DEWA premise number. This is usually displayed on the property door or provided by the landlord, agent, or building management.
- Your Emirates ID if available.
- Passport/visa details if requested during setup.
- Payment method for deposit and activation charges.

### Step-by-step setup

1. **Confirm the property details**
   - Ask the agent, landlord, or building management for the correct unit details.
   - Confirm the DEWA premise number before applying.
   - Make sure the property is the exact unit you are renting, not just the building.

2. **Complete or start Ejari**
   - DEWA move-in is closely connected to tenancy registration.
   - In many rental flows, the Ejari process and DEWA activation are linked.
   - Do not leave DEWA activation until the day you physically move in.

3. **Open the DEWA Move-In service**
   - Use the official DEWA Move-In service page.
   - Select the move-in / activation service.
   - Enter the required property and tenancy details.

4. **Check the account and premise information**
   - Review the premise number, unit number, and tenant information carefully.
   - Small mistakes can delay activation.

5. **Pay the required charges**
   - Pay the security deposit and activation charges shown by DEWA.
   - Keep the receipt or payment confirmation.
   - Do not rely on estimated figures from unofficial blogs because charges can change.

6. **Wait for activation**
   - DEWA states that if supply is not activated within 15 working hours after security deposit payment, users should contact Customer Care.
   - Save your DEWA account number and confirmation email.

7. **After activation**
   - Create or log in to your DEWA online account.
   - Check your first bill carefully.
   - Save your account details for future move-out, deposit refund, or bill payments.

### Common mistakes to avoid

- Applying with the wrong premise number.
- Waiting until move-in day to activate.
- Assuming the landlord has already transferred utilities.
- Forgetting to keep payment receipts.
- Using unofficial fee information without checking DEWA.

### Official links

- [DEWA Move-In service](https://dewa.gov.ae/en/consumer/supply-management/activation-of-electricity-water-move-in)
- [DEWA official website](https://www.dewa.gov.ae/)
""",
    },
    "Ejari": {
        "icon": "E",
        "subtitle": "Tenancy contract registration",
        "description": (
            "Register your tenancy contract through Dubai Land Department systems."
        ),
        "official_links": [
            ("Dubai Land Department - Register / Renew Ejari Contract", "https://dubailand.gov.ae/en/eservices/register-renew-ejari-contract/"),
            ("Dubai REST app information", "https://dubailand.gov.ae/"),
        ],
        "content": """
### What this is

Ejari is Dubai’s tenancy contract registration system. It is important because it formally registers your rental contract and is often needed for utility activation and other residence-related processes.

### Before you start

Prepare or confirm:

- Signed tenancy contract.
- Tenant Emirates ID, if available.
- Tenant passport and visa details if requested.
- Landlord details.
- Title deed or property ownership details if requested.
- DEWA premise number if required.
- Payment method.
- Access to Dubai REST / Ejari system, or visit an authorised centre.

### Step-by-step setup

1. **Sign the tenancy contract first**
   - Do not try to register Ejari before the rental contract is signed.
   - Check that names, unit number, rent amount, and contract dates are correct.

2. **Choose registration method**
   You usually have a few routes:
   - Dubai REST / Ejari online route.
   - Real Estate Trustee Centre.
   - Property management company, if the property is managed by one.
   - Authorised service channel.

3. **Submit documents**
   - Upload or submit the tenancy contract and required documents.
   - Make sure there are no missing pages or mismatched details.
   - The name on the contract should match the tenant documents.

4. **Pay service fees**
   - Pay the service fees shown by the official channel.
   - Fees can vary depending on the channel, so use the official amount shown during registration.

5. **Wait for review / approval**
   - Dubai Land Department explains that an employee may review and approve the request through the system.
   - Once approved, the e-contract registration certificate is issued.

6. **Save your Ejari certificate**
   - Download the PDF certificate.
   - Save it in your relocation folder.
   - You may need it for DEWA, internet setup, bank address updates, school registration, or other move-in processes.

### Common mistakes to avoid

- Signing a contract with incorrect unit details.
- Not checking landlord/property details.
- Uploading unclear document scans.
- Assuming Ejari is optional.
- Waiting until another service asks for it.

### Official links

- [Dubai Land Department - Register / Renew Ejari Contract](https://dubailand.gov.ae/en/eservices/register-renew-ejari-contract/)
- [Dubai Land Department official website](https://dubailand.gov.ae/)
""",
    },
    "e& Home Internet": {
        "icon": "e&",
        "subtitle": "eLife / home internet setup or move",
        "description": (
            "Set up or move e& home internet when you settle into a Dubai property."
        ),
        "official_links": [
            ("e& Home Move", "https://www.eand.ae/en/c/home/home-moving.html"),
            ("e& UAE official website", "https://www.eand.ae/"),
        ],
        "content": """
### What this is

e& provides home internet, TV, and landline packages in the UAE. If you already have an eLife plan and are moving, e& has a Home Move flow. If you are new, you can compare available home plans and request installation.

### Before you start

Prepare or confirm:

- New home address and unit details.
- Building name and community.
- Tenancy contract or proof of residence if requested.
- Emirates ID, if available.
- Current e& account details if you are moving an existing service.
- Preferred installation date and time.
- Router/equipment details if you already have an existing connection.

### Step-by-step setup for an existing e& customer moving home

1. **Check whether your current plan can move**
   - Confirm if your current eLife/home plan can be relocated to the new address.
   - Check if your new building supports the required e& service.

2. **Use the e& UAE app**
   - e& describes its Home Move flow as: download the e& UAE app, go to the eLife Plan tab, tap Manage, then tap Home Move and follow the instructions.

3. **Enter the new address**
   - Add the building, unit, and area details carefully.
   - Wrong unit details can delay installation.

4. **Upload documents if requested**
   - Upload tenancy contract, Emirates ID, or other proof requested by the app.
   - Use clear scans/photos.

5. **Book the technician visit**
   - Select a suitable installation or relocation slot.
   - Make sure someone can access the apartment and telecom room if required.

6. **Prepare equipment**
   - Keep router, ONT device, TV box, remote, cables, and account details available.
   - Do not throw away existing equipment before confirming with e&.

7. **Test after installation**
   - Test Wi-Fi speed in multiple rooms.
   - Check TV/landline if included.
   - Save support ticket/reference number.

### If you are a new e& customer

1. Compare home internet packages on the official e& website.
2. Check whether the building supports the selected plan.
3. Prepare Emirates ID and tenancy/proof of residence if requested.
4. Book installation.
5. Test speed after activation.

### Common mistakes to avoid

- Booking installation before confirming building coverage.
- Not being available for the technician visit.
- Forgetting router/equipment from the previous home.
- Choosing speed only by price without checking contract terms.
- Not checking cancellation or relocation fees.

### Official links

- [e& Home Move](https://www.eand.ae/en/c/home/home-moving.html)
- [e& UAE official website](https://www.eand.ae/)
""",
    },
    "du Home Internet": {
        "icon": "du",
        "subtitle": "du home internet setup or relocation",
        "description": (
            "Set up or move du home internet, TV, and landline services."
        ),
        "official_links": [
            ("du Home Relocation", "https://www.du.ae/personal/at-home/moving-to-a-new-home"),
            ("du official website", "https://www.du.ae/"),
        ],
        "content": """
### What this is

du provides home internet, TV, and landline services in the UAE. If you already have du Home and are moving, du offers an online home relocation service.

### Before you start

Prepare or confirm:

- New address and unit number.
- Building/community name.
- Tenancy contract or title deed.
- Proof of relationship if the tenancy is not in your name.
- Emirates ID, if available.
- Current du account details if relocating.
- Preferred installation date and time.

### Step-by-step setup for moving an existing du Home service

1. **Check your new building**
   - Confirm whether du service is available in the building.
   - Ask building management if the telecom infrastructure is ready.

2. **Open du Home relocation**
   - Use the official du Home relocation page.
   - Start the relocation request online.

3. **Upload required documents**
   - du states that users may need to upload the tenancy contract or title deed for the new home.
   - If the tenancy is not in your name, upload proof of relationship if requested.

4. **Review the relocation fee**
   - du states that a moving fee of AED 100 will be charged on the next bill.
   - Always confirm the final amount during the official request flow.

5. **Choose installation timing**
   - Pick a technician visit time.
   - Make sure someone has access to the apartment and telecom area.

6. **Prepare existing devices**
   - Keep router, TV box, landline device, remote, cables, and power adapters ready.
   - Confirm whether you need to return, reuse, or replace any device.

7. **Test the service**
   - Test Wi-Fi, TV, and landline if included.
   - Save confirmation SMS/email and support reference.

### If you are a new du customer

1. Compare du Home plans on the official du website.
2. Check building coverage.
3. Prepare Emirates ID and tenancy/title deed if requested.
4. Book installation.
5. Test speed and Wi-Fi coverage after setup.

### Common mistakes to avoid

- Assuming every building supports both du and e& equally.
- Forgetting to upload proof of relationship when the tenancy is under another person’s name.
- Ignoring contract period and early termination terms.
- Missing technician appointment.
- Not testing Wi-Fi in bedrooms and work areas.

### Official links

- [du Home relocation](https://www.du.ae/personal/at-home/moving-to-a-new-home)
- [du official website](https://www.du.ae/)
""",
    },
    "Mobile SIM / eSIM": {
        "icon": "SIM",
        "subtitle": "du / e& mobile setup",
        "description": (
            "Get connected with a UAE mobile number through tourist, prepaid, postpaid, SIM, or eSIM options."
        ),
        "official_links": [
            ("TDRA Mobile Consumer Registration", "https://tdra.gov.ae/en/initiatives/registration-for-mobile-consumers"),
            ("e& Visitor Line", "https://www.eand.ae/en/c/mobile/plans/visitor-line.html"),
            ("du Tourist SIM", "https://shop.du.ae/en/personal/prepaid/du-tourist-prepaid-plans?view=bundles"),
            ("e& Mobile Registration Renewal", "https://www.eand.ae/en/c/mobile-registration-renewal.html"),
            ("du Emirates ID update", "https://www.du.ae/support/id-renewal"),
        ],
        "content": """
### What this is

This guide helps newcomers choose and activate a UAE mobile line. You may start with a tourist SIM/eSIM if you have just arrived, then move to a resident prepaid or postpaid plan later once your Emirates ID is available.

### Before you start

Prepare or confirm:

- Passport if you are a visitor/tourist.
- Emirates ID if you are a UAE resident.
- UAE PASS access if using digital services.
- eSIM-compatible phone if choosing eSIM.
- Unlocked phone that supports UAE networks.
- Payment card or cash depending on channel.

### Step-by-step setup for visitors

1. **Choose tourist SIM or eSIM**
   - e& and du both offer visitor/tourist mobile options.
   - Tourist lines are useful when you need data immediately after landing.

2. **Prepare passport identification**
   - Visitors usually register using passport details.
   - Keep the same passport used for entry.

3. **Activate the line**
   - Follow the provider’s activation steps.
   - For eSIM, make sure your phone supports eSIM and is not carrier locked.
   - For physical SIM, insert the SIM and follow activation instructions.

4. **Choose data package**
   - Select a package based on your stay length, maps usage, WhatsApp/calls, hotspot needs, and delivery apps.

5. **Track validity**
   - Tourist SIMs usually have validity limits.
   - Set a reminder before expiry if you still need the number.

### Step-by-step setup for residents

1. **Wait for or prepare Emirates ID**
   - Emirates ID is the main identity document for UAE residents.
   - Telecom providers require valid identity registration.

2. **Choose prepaid or postpaid**
   - Prepaid is flexible and easier for early arrival.
   - Postpaid may be better after stable residency, salary, and address details.

3. **Register the number**
   - Use the provider’s app, website, or store.
   - Upload or scan Emirates ID if requested.

4. **Keep registration updated**
   - e& states that maintaining valid Emirates ID registration is required and non-renewal may result in suspension/disconnection.
   - du also provides an Emirates ID update flow for customers.

5. **Save account access**
   - Download provider app.
   - Enable usage tracking.
   - Disable unwanted auto-renewal or third-party subscriptions.

### Common mistakes to avoid

- Buying a plan before checking phone compatibility.
- Forgetting tourist SIM validity.
- Not updating Emirates ID after renewal.
- Ignoring auto-renewal settings.
- Using unofficial sellers or unknown SIM sources.

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
        "subtitle": "Digital identity setup",
        "description": (
            "Set up UAE PASS to access many UAE digital government and partner services."
        ),
        "official_links": [
            ("UAE PASS official website", "https://uaepass.ae/"),
            ("UAE Government - Emirates ID", "https://u.ae/en/information-and-services/visa-and-emirates-id/emirates-id"),
        ],
        "content": """
### What this is

UAE PASS is the UAE’s national digital identity platform. It helps residents, citizens, and visitors access many online services and digitally sign or verify documents.

### Why it matters for relocation

UAE PASS can make many digital processes easier, especially when dealing with government or semi-government services. It is useful for identity verification, document access, and logging into supported portals.

### Before you start

Prepare or confirm:

- Smartphone.
- UAE mobile number.
- Emirates ID if you are a resident.
- Passport/visitor details if supported for your case.
- Access to the UAE PASS app.
- Ability to verify identity through the official process.

### Step-by-step setup

1. **Download the UAE PASS app**
   - Use the official app store listing.
   - Avoid unofficial links.

2. **Register your account**
   - Enter your details as requested.
   - Use your own mobile number.

3. **Verify your identity**
   - Follow the app’s identity verification flow.
   - Residents may need Emirates ID details.

4. **Set up secure access**
   - Create a secure PIN.
   - Enable biometrics if available.
   - Do not share your PIN or OTP.

5. **Use UAE PASS for supported services**
   - Log in to supported government and partner platforms.
   - Use digital signature features only when you understand the document.

### Common mistakes to avoid

- Using someone else’s mobile number.
- Sharing OTPs or PINs.
- Skipping identity verification and expecting full access.
- Using UAE PASS on a shared phone.
- Signing documents without reading them.

### Official links

- [UAE PASS official website](https://uaepass.ae/)
- [UAE Government - Emirates ID](https://u.ae/en/information-and-services/visa-and-emirates-id/emirates-id)
""",
    },
}


@st.dialog("Hayyak utility guide")
def show_utility_modal(name, item):
    st.subheader(name)
    st.caption(item["subtitle"])
    arabic_divider()

    st.markdown(item["content"])

    st.divider()
    st.caption(
        "Hayyak note: official processes, fees, required documents, and timelines can change. "
        "Always confirm details through the linked official service before applying."
    )


st.markdown(
    """
    <section class="section-card">
        <div class="section-heading">
            <div>
                <h2>Utilities and move-in setup</h2>
                <p>
                    Choose a setup area to view a detailed, step-by-step guide.
                    Each guide is designed for newcomers moving into a Dubai home.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


cols = st.columns(3)
items = list(UTILITIES.items())

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

        if st.button(f"View {name} guide", key=f"utility_{name}"):
            show_utility_modal(name, item)
