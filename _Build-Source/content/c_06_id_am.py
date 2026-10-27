# -*- coding: utf-8 -*-
# ID.AM Asset Management
C = {}

C["ID-STD-001"] = dict(
 purpose=("This standard sets requirements for identifying, recording, classifying, owning, and managing information assets throughout their life cycle (ID.AM).",
          "มาตรฐานนี้กำหนดข้อกำหนดในการระบุ บันทึก จัดชั้น กำหนดเจ้าของ และบริหารจัดการทรัพย์สินสารสนเทศตลอดวงจรชีวิต (ID.AM)"),
 sections=[
  ("Asset Categories and Inventories", "ประเภททรัพย์สินและทะเบียน", "Define asset categories and the inventory where each is recorded.", "กำหนดประเภททรัพย์สินและทะเบียนที่ใช้บันทึกแต่ละประเภท",
   {"t": ["Category", "Examples", "Inventory"], "r": [
     ["Hardware", "Servers, endpoints, network devices, mobile devices", "ID-REG-001"], ["Software and services", "Applications, operating systems, SaaS, cloud services", "ID-REG-002"],
     ["Data", "Databases, file shares, data sets with personal data", "ID-REG-003, GV-REG-007"], ["OT and medical devices", "Building systems, medical and lab devices", "ID-REG-004"],
     ["Supplier services", "Outsourced and cloud services", "GV-REG-009"]], "w": [4.0, 7.5, 5.0]},
   {"t": ["ประเภท", "ตัวอย่าง", "ทะเบียน"], "r": [
     ["ฮาร์ดแวร์", "เซิร์ฟเวอร์ อุปกรณ์ปลายทาง อุปกรณ์เครือข่าย อุปกรณ์เคลื่อนที่", "ID-REG-001"], ["ซอฟต์แวร์และบริการ", "แอปพลิเคชัน ระบบปฏิบัติการ SaaS บริการคลาวด์", "ID-REG-002"],
     ["ข้อมูล", "ฐานข้อมูล พื้นที่แชร์ไฟล์ ชุดข้อมูลที่มีข้อมูลส่วนบุคคล", "ID-REG-003, GV-REG-007"], ["OT และอุปกรณ์การแพทย์", "ระบบอาคาร อุปกรณ์การแพทย์และห้องปฏิบัติการ", "ID-REG-004"],
     ["บริการจากผู้ให้บริการ", "บริการจ้างภายนอกและบริการคลาวด์", "GV-REG-009"]], "w": [4.0, 7.5, 5.0]}),
  ("Requirements", "ข้อกำหนด", "Set measurable asset management requirements.", "กำหนดข้อกำหนดการบริหารทรัพย์สินที่วัดผลได้",
   {"t": ["ID", "Requirement"], "r": [
     ["AM-01", "Every asset is recorded in the correct inventory before connection to the network or use in production."],
     ["AM-02", "Every asset has a named owner responsible for its protection and life cycle."],
     ["AM-03", "Each asset has a criticality rating (Critical, High, Medium, Low) derived from the BIA (ID-RPT-002) and a data classification (PR-STD-004) (ID.AM-05)."],
     ["AM-04", "Automated discovery reconciles inventories at least monthly; unknown devices are investigated within 5 working days."],
     ["AM-05", "Inventories record end-of-support dates; assets reaching end of support have a replacement plan or an approved exception."],
     ["AM-06", "Assets are returned on termination and disposed of securely (ID-PRC-001)."]], "w": [1.8, 14.7]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["AM-01", "บันทึกทรัพย์สินทุกรายการในทะเบียนที่ถูกต้องก่อนเชื่อมต่อเครือข่ายหรือใช้งานจริง"],
     ["AM-02", "ทรัพย์สินทุกรายการมีเจ้าของที่ระบุชื่อ ซึ่งรับผิดชอบการปกป้องและวงจรชีวิตของทรัพย์สิน"],
     ["AM-03", "ทรัพย์สินแต่ละรายการมีระดับความสำคัญ (วิกฤต สูง ปานกลาง ต่ำ) จาก BIA (ID-RPT-002) และระดับชั้นข้อมูล (PR-STD-004) (ID.AM-05)"],
     ["AM-04", "ใช้เครื่องมือค้นหาอัตโนมัติกระทบยอดทะเบียนอย่างน้อยทุกเดือน และสอบสวนอุปกรณ์ที่ไม่รู้จักภายใน 5 วันทำการ"],
     ["AM-05", "ทะเบียนบันทึกวันสิ้นสุดการสนับสนุน ทรัพย์สินที่ใกล้หมดการสนับสนุนต้องมีแผนทดแทนหรือข้อยกเว้นที่อนุมัติ"],
     ["AM-06", "คืนทรัพย์สินเมื่อพ้นสภาพ และทำลายหรือจำหน่ายอย่างมั่นคงปลอดภัย (ID-PRC-001)"]], "w": [1.8, 14.7]}),
 ],
 bp=[("Use one configuration management database (CMDB) or asset tool as the source of truth, fed by discovery tools.", "ใช้ฐานข้อมูลการจัดการคอนฟิกูเรชัน (CMDB) หรือเครื่องมือบริหารทรัพย์สินเพียงแหล่งเดียวเป็นข้อมูลอ้างอิงหลัก โดยรับข้อมูลจากเครื่องมือค้นหาอัตโนมัติ"),
     ("Start with critical assets and expand coverage; a complete but stale inventory is less useful than an accurate partial one.", "เริ่มจากทรัพย์สินสำคัญแล้วขยายขอบเขต ทะเบียนที่ครบแต่ล้าสมัยมีประโยชน์น้อยกว่าทะเบียนที่ถูกต้องแม้ยังไม่ครบ"),
     ("Link inventory records to vulnerability and patch data to show exposure per asset.", "เชื่อมข้อมูลทะเบียนกับข้อมูลช่องโหว่และแพตช์ เพื่อแสดงความเสี่ยงของทรัพย์สินแต่ละรายการ")],
 mistakes=[("Finance asset register is used as the security inventory; it misses software, cloud, and leased devices.", "ใช้ทะเบียนทรัพย์สินของฝ่ายการเงินเป็นทะเบียนด้านความมั่นคงปลอดภัย ซึ่งไม่ครอบคลุมซอฟต์แวร์ คลาวด์ และอุปกรณ์เช่า")],
)

C["ID-PRC-001"] = dict(
 purpose=("This procedure manages assets from request and acquisition through deployment, maintenance, transfer, and secure disposal (ID.AM-08, PR.PS-03).",
          "ระเบียบปฏิบัตินี้บริหารทรัพย์สินตั้งแต่การขอและการจัดหา การติดตั้ง การบำรุงรักษา การโอนย้าย จนถึงการทำลายหรือจำหน่ายอย่างมั่นคงปลอดภัย (ID.AM-08, PR.PS-03)"),
 sections=[
  ("Life-Cycle Steps", "ขั้นตอนตลอดวงจรชีวิต", "Describe each stage with actor and controls.", "อธิบายแต่ละขั้นตอนพร้อมผู้ดำเนินการและมาตรการควบคุม",
   {"t": ["Stage", "Activity and control", "Actor"], "r": [
     ["Request and acquire", "Approve need; apply Secure Acquisition Standard (GV-STD-003)", "Requester, [PROC]"],
     ["Receive and register", "Tag the asset and record it in the inventory with owner and criticality", "[ITM]"],
     ["Deploy", "Apply the secure configuration baseline (PR-STD-010) and enroll in management tools", "[ITM]"],
     ["Maintain", "Patch, maintain under vendor support, and review warranty and end-of-support dates", "[ITM]"],
     ["Transfer", "Update owner and location; wipe before reassignment", "[ITM]"],
     ["Retire and dispose", "Sanitize media per NIST SP 800-88, record in ID-FRM-001, update inventory", "[ITM]"]], "w": [3.5, 9.5, 3.5]},
   {"t": ["ขั้นตอน", "กิจกรรมและมาตรการควบคุม", "ผู้ดำเนินการ"], "r": [
     ["ขอและจัดหา", "อนุมัติความต้องการ และใช้มาตรฐานการจัดหาอย่างมั่นคงปลอดภัย (GV-STD-003)", "ผู้ขอ [PROC]"],
     ["รับและลงทะเบียน", "ติดป้ายทรัพย์สินและบันทึกในทะเบียน พร้อมเจ้าของและระดับความสำคัญ", "[ITM]"],
     ["ติดตั้งใช้งาน", "ตั้งค่าตามมาตรฐานการตั้งค่าระบบ (PR-STD-010) และลงทะเบียนในเครื่องมือบริหารจัดการ", "[ITM]"],
     ["บำรุงรักษา", "ติดตั้งแพตช์ บำรุงรักษาภายใต้การสนับสนุนของผู้ขาย และทบทวนวันหมดประกันและวันสิ้นสุดการสนับสนุน", "[ITM]"],
     ["โอนย้าย", "ปรับปรุงเจ้าของและสถานที่ ล้างข้อมูลก่อนส่งต่อ", "[ITM]"],
     ["ปลดระวางและจำหน่าย", "ทำลายข้อมูลบนสื่อตาม NIST SP 800-88 บันทึกใน ID-FRM-001 และปรับปรุงทะเบียน", "[ITM]"]], "w": [3.5, 9.5, 3.5]}),
 ],
 bp=[("Use certified disposal vendors and obtain certificates of destruction with serial numbers.", "ใช้ผู้ให้บริการทำลายที่ได้รับการรับรอง และขอหนังสือรับรองการทำลายที่ระบุหมายเลขเครื่อง"),
     ("Block network access for devices not in the inventory using network access control (NAC).", "บล็อกการเข้าถึงเครือข่ายของอุปกรณ์ที่ไม่อยู่ในทะเบียนด้วยระบบควบคุมการเข้าถึงเครือข่าย (NAC)")],
 mistakes=[("Returning leased copiers or medical devices with patient data still on their hard drives.", "ส่งคืนเครื่องถ่ายเอกสารหรืออุปกรณ์การแพทย์ที่เช่าโดยยังมีข้อมูลผู้ป่วยอยู่ในฮาร์ดดิสก์")],
)

C["ID-REG-001"] = dict(
 purpose=("This inventory records all hardware managed by the organization, with owner, location, criticality, and support status (ID.AM-01).",
          "ทะเบียนนี้บันทึกฮาร์ดแวร์ทั้งหมดที่องค์กรบริหารจัดการ พร้อมเจ้าของ สถานที่ ระดับความสำคัญ และสถานะการสนับสนุน (ID.AM-01)"),
 fields=[
  ("Asset ID", "รหัสทรัพย์สิน", "Unique tag.", "ป้ายรหัสที่ไม่ซ้ำ", "SRV-APP-014"),
  ("Type and model", "ประเภทและรุ่น", "Such as server, laptop, or switch.", "เซิร์ฟเวอร์ โน้ตบุ๊ก สวิตช์ ฯลฯ", ""),
  ("Hostname and IP", "ชื่อเครื่องและ IP", "Network identifiers.", "ข้อมูลระบุตัวตนบนเครือข่าย", ""),
  ("Location", "สถานที่", "Site and room.", "อาคารและห้อง", ""),
  ("Owner", "เจ้าของ", "Accountable role.", "บทบาทที่รับผิดชอบ", ""),
  ("Criticality", "ระดับความสำคัญ", "Critical, High, Medium, Low.", "วิกฤต สูง ปานกลาง ต่ำ", ""),
  ("Operating system", "ระบบปฏิบัติการ", "Name and version.", "ชื่อและรุ่น", ""),
  ("End of support", "วันสิ้นสุดการสนับสนุน", "Vendor date.", "วันที่ตามผู้ขาย", ""),
  ("Status", "สถานะ", "In use, Spare, Retired.", "ใช้งาน สำรอง ปลดระวาง", ""),
 ],
 rows=[
  ["SRV-HIS-DB01", "Database server, rack", "his-db01 / 10.10.20.11", "Riverside data center, Rack A3", "IT Infrastructure Manager", "Critical", "Linux (supported release)", "06/2029", "In use"],
  ["SRV-HIS-APP01", "Application server, virtual", "his-app01 / 10.10.20.21", "Riverside data center", "IT Infrastructure Manager", "Critical", "Windows Server 2022", "10/2031", "In use"],
  ["NET-CORE-01", "Core switch", "core-sw01 / 10.0.0.1", "Riverside data center", "IT Infrastructure Manager", "Critical", "Vendor network OS", "12/2028", "In use"],
  ["WS-ER-012", "Clinical workstation", "er-ws012 / DHCP", "Riverside Emergency Department", "IT Service Desk Lead", "High", "Windows 11", "Supported", "In use"],
  ["SRV-NC-01", "Nurse call server", "nc-srv01 / 10.30.5.10", "Nonthaburi Building B", "Facilities and Engineering Manager", "High", "Windows Server 2012 R2", "10/2023 (exception EXC-2026-002)", "In use"],
 ],
 cmc_note="CMC's hardware inventory holds about 2,600 records across both hospitals and is reconciled monthly against endpoint management and network discovery data.",
 bp=[("Populate the inventory automatically from endpoint management, hypervisors, and network scans.", "นำเข้าข้อมูลทะเบียนโดยอัตโนมัติจากระบบบริหารอุปกรณ์ปลายทาง ไฮเปอร์ไวเซอร์ และการสแกนเครือข่าย"),
     ("Flag end-of-support assets automatically 12 months in advance.", "แจ้งเตือนทรัพย์สินที่จะหมดการสนับสนุนล่วงหน้า 12 เดือนโดยอัตโนมัติ")],
 mistakes=[("Recording only servers and forgetting network, printers, and IoT devices.", "บันทึกเฉพาะเซิร์ฟเวอร์และลืมอุปกรณ์เครือข่าย เครื่องพิมพ์ และอุปกรณ์ IoT")],
)

C["ID-REG-002"] = dict(
 purpose=("This inventory records software, applications, and services (including SaaS and supplier-provided services), with owner, criticality, data, and support status (ID.AM-02, ID.AM-04).",
          "ทะเบียนนี้บันทึกซอฟต์แวร์ แอปพลิเคชัน และบริการ (รวมถึง SaaS และบริการจากผู้ให้บริการ) พร้อมเจ้าของ ระดับความสำคัญ ข้อมูล และสถานะการสนับสนุน (ID.AM-02, ID.AM-04)"),
 fields=[
  ("System ID", "รหัสระบบ", "Unique reference.", "รหัสอ้างอิง", "APP-001"),
  ("System or service", "ระบบหรือบริการ", "Name and purpose.", "ชื่อและวัตถุประสงค์", ""),
  ("System owner", "เจ้าของระบบ", "Business owner.", "เจ้าของธุรกิจ", ""),
  ("Hosting", "การติดตั้ง", "On-premises, private cloud, SaaS.", "ภายในองค์กร คลาวด์ส่วนตัว SaaS", ""),
  ("Supplier", "ผู้ให้บริการ", "Link to GV-REG-009.", "เชื่อมโยงกับ GV-REG-009", ""),
  ("Criticality and RTO", "ระดับความสำคัญและ RTO", "From the BIA.", "จาก BIA", ""),
  ("Highest data class", "ชั้นข้อมูลสูงสุด", "Per PR-STD-004.", "ตาม PR-STD-004", ""),
  ("Version and support", "รุ่นและการสนับสนุน", "Current version and end of support.", "รุ่นปัจจุบันและวันสิ้นสุดการสนับสนุน", ""),
  ("Authentication", "การยืนยันตัวตน", "SSO, MFA, local.", "SSO MFA หรือบัญชีภายใน", ""),
 ],
 rows=[
  ["APP-001", "Hospital Information System (HIS)", "CIO with Medical Director", "On-premises", "SUP-001 HIS Vendor A", "Critical, RTO 4 hours", "Restricted (patient data)", "v12.3, supported to 2029", "Directory login; MFA for remote and admin"],
  ["APP-002", "Picture Archiving and Communication System (PACS)", "Director of Radiology", "On-premises", "SUP-002 PACS Vendor B", "Critical, RTO 8 hours", "Restricted", "v8.1, supported to 2028", "Local accounts (SSO planned 2027)"],
  ["APP-003", "Laboratory Information System (LIS)", "Laboratory Director", "On-premises", "SUP-003 LIS Vendor C", "Critical, RTO 8 hours", "Restricted", "v5.4, supported", "Directory login"],
  ["APP-004", "ERP (finance, procurement, HR)", "CFO", "Private cloud", "SUP-007 ERP host", "High, RTO 24 hours", "Confidential", "Supported", "SSO with MFA"],
  ["APP-005", "Microsoft 365 (email, Teams, SharePoint)", "CIO", "SaaS", "SUP-005 Microsoft", "High, RTO 8 hours", "Confidential", "Evergreen", "SSO with MFA"],
  ["APP-006", "Patient portal", "Director of Patient Experience", "Public cloud", "In-house development", "Medium, RTO 24 hours", "Restricted", "v2.0", "Patient accounts with OTP"],
 ],
 bp=[("Use cloud access discovery to find unsanctioned SaaS and bring it under governance.", "ใช้เครื่องมือค้นหาการใช้งานคลาวด์เพื่อค้นหา SaaS ที่ไม่ได้รับอนุญาต และนำเข้าสู่การกำกับดูแล"),
     ("Record integrations and interfaces between systems; they are frequent attack paths.", "บันทึกการเชื่อมต่อระหว่างระบบ เพราะเป็นช่องทางโจมตีที่พบบ่อย")],
 mistakes=[("Listing applications without owners, so no one approves access or accepts risk.", "ระบุแอปพลิเคชันโดยไม่มีเจ้าของ ทำให้ไม่มีผู้อนุมัติสิทธิ์หรือยอมรับความเสี่ยง")],
)

C["ID-REG-003"] = dict(
 purpose=("This register records important data sets, where they are stored, their classification, owners, and how data flows between systems and parties (ID.AM-03, ID.AM-07).",
          "ทะเบียนนี้บันทึกชุดข้อมูลสำคัญ ที่จัดเก็บ ระดับชั้นข้อมูล เจ้าของ และการไหลของข้อมูลระหว่างระบบและบุคคลภายนอก (ID.AM-03, ID.AM-07)"),
 fields=[
  ("Data set ID", "รหัสชุดข้อมูล", "Unique reference.", "รหัสอ้างอิง", "DATA-001"),
  ("Data set", "ชุดข้อมูล", "Description.", "คำอธิบาย", ""),
  ("Classification", "ชั้นข้อมูล", "Per PR-STD-004.", "ตาม PR-STD-004", ""),
  ("Personal data (ROPA link)", "ข้อมูลส่วนบุคคล (เชื่อมโยง ROPA)", "ROPA ID if personal data.", "รหัส ROPA กรณีเป็นข้อมูลส่วนบุคคล", ""),
  ("Data owner", "เจ้าของข้อมูล", "Role.", "บทบาท", ""),
  ("Storage location", "ที่จัดเก็บ", "System and location.", "ระบบและสถานที่", ""),
  ("Flows to", "ไหลไปยัง", "Systems or parties receiving the data and method.", "ระบบหรือบุคคลที่รับข้อมูลและวิธีการ", ""),
  ("Protection in transit", "การปกป้องขณะส่ง", "Encryption method.", "วิธีการเข้ารหัส", ""),
 ],
 rows=[
  ["DATA-001", "Electronic medical record", "Restricted", "ROPA-MR-01", "Director of Medical Records", "HIS database, Riverside data center", "PACS and LIS (HL7 interface); insurers (portal)", "TLS on interfaces; insurer portal HTTPS"],
  ["DATA-002", "Diagnostic images", "Restricted", "ROPA-IMG-01", "Director of Radiology", "PACS storage", "Referring hospitals (secure image exchange)", "TLS 1.2 or higher"],
  ["DATA-003", "Payroll data", "Confidential", "ROPA-HR-01", "HR Director", "ERP (private cloud)", "Bank (payroll file via secure file transfer)", "SFTP with encryption"],
  ["DATA-004", "Security logs", "Confidential", "Not applicable (staff identifiers)", "Security Manager", "Log platform", "MSSP (log forwarding)", "TLS"],
 ],
 bp=[("Draw a data flow diagram for each critical system and keep it with the register.", "จัดทำแผนภาพการไหลของข้อมูลสำหรับระบบสำคัญแต่ละระบบ และเก็บไว้ร่วมกับทะเบียน"),
     ("Use the same identifiers as the ROPA so privacy and security views stay aligned.", "ใช้รหัสเดียวกับ ROPA เพื่อให้มุมมองด้านความเป็นส่วนตัวและความมั่นคงปลอดภัยสอดคล้องกัน")],
 mistakes=[("Ignoring unstructured data in file shares and email, where much sensitive data actually sits.", "ละเลยข้อมูลที่ไม่มีโครงสร้างในพื้นที่แชร์ไฟล์และอีเมล ซึ่งเป็นที่อยู่ของข้อมูลอ่อนไหวจำนวนมาก")],
)

C["ID-RPT-001"] = dict(
 purpose=("This document shows the authorized network architecture, security zones, and data flows, so that changes, risks, and incidents can be assessed against a known baseline (ID.AM-03).",
          "เอกสารนี้แสดงสถาปัตยกรรมเครือข่ายที่ได้รับอนุญาต โซนความมั่นคงปลอดภัย และการไหลของข้อมูล เพื่อใช้เป็นฐานในการประเมินการเปลี่ยนแปลง ความเสี่ยง และเหตุการณ์ (ID.AM-03)"),
 sections=[
  ("Security Zones", "โซนความมั่นคงปลอดภัย", "Define network zones, their trust level, and allowed connections.", "กำหนดโซนเครือข่าย ระดับความน่าเชื่อถือ และการเชื่อมต่อที่อนุญาต",
   {"t": ["Zone", "Contents", "Trust", "Allowed inbound from"], "r": [
     ["Internet", "Public networks", "Untrusted", "Not applicable"], ["DMZ", "Public web, email gateway, reverse proxy", "Low", "Internet (specific ports)"],
     ["Server zone", "Business applications and databases", "High", "User zone (application ports), management zone"], ["User zone", "Workstations, printers", "Medium", "Management zone"],
     ["Management zone", "Admin jump hosts, monitoring", "High", "Privileged users through MFA"], ["Guest zone", "Guest Wi-Fi", "Untrusted", "None (internet only)"]], "w": [3.0, 5.5, 2.5, 5.5]},
   {"t": ["โซน", "สิ่งที่อยู่ในโซน", "ความน่าเชื่อถือ", "อนุญาตให้เชื่อมต่อเข้าจาก"], "r": [
     ["อินเทอร์เน็ต", "เครือข่ายสาธารณะ", "ไม่น่าเชื่อถือ", "ไม่เกี่ยวข้อง"], ["DMZ", "เว็บสาธารณะ เกตเวย์อีเมล Reverse proxy", "ต่ำ", "อินเทอร์เน็ต (เฉพาะพอร์ตที่กำหนด)"],
     ["โซนเซิร์ฟเวอร์", "แอปพลิเคชันทางธุรกิจและฐานข้อมูล", "สูง", "โซนผู้ใช้ (พอร์ตแอปพลิเคชัน) และโซนบริหารจัดการ"], ["โซนผู้ใช้", "เครื่องคอมพิวเตอร์ เครื่องพิมพ์", "ปานกลาง", "โซนบริหารจัดการ"],
     ["โซนบริหารจัดการ", "Jump host สำหรับผู้ดูแลระบบ ระบบเฝ้าระวัง", "สูง", "ผู้มีสิทธิ์ระดับสูงผ่าน MFA"], ["โซนผู้มาติดต่อ", "Wi-Fi สำหรับผู้มาติดต่อ", "ไม่น่าเชื่อถือ", "ไม่มี (ออกอินเทอร์เน็ตเท่านั้น)"]], "w": [3.0, 5.5, 2.5, 5.5]},
   {"t": ["Zone", "Contents", "Trust", "Allowed inbound from"], "r": [
     ["Internet", "Public networks", "Untrusted", "Not applicable"], ["DMZ", "Patient portal reverse proxy, email gateway", "Low", "Internet (HTTPS, SMTP)"],
     ["Clinical server zone", "HIS, PACS, LIS, interface engine", "High", "Clinical user zone (application ports), management zone"],
     ["Medical device zone", "Imaging modalities, lab analyzers, infusion pump gateways", "Restricted", "PACS and LIS servers only (DICOM, HL7)"],
     ["Clinical and office user zones", "Workstations, printers", "Medium", "Management zone"], ["Management zone", "PAM jump hosts, monitoring", "High", "Admins and vendors via MFA and session recording"],
     ["Patient and guest Wi-Fi", "Internet only", "Untrusted", "None"]], "w": [3.0, 5.5, 2.5, 5.5]}),
  ("Diagram and Data Flows", "แผนภาพและการไหลของข้อมูล", "Provide a current diagram showing zones, firewalls, external connections, and critical data flows.", "จัดทำแผนภาพปัจจุบันที่แสดงโซน ไฟร์วอลล์ การเชื่อมต่อภายนอก และการไหลของข้อมูลสำคัญ",
   ["Insert the network diagram (logical) showing zones, firewalls, internet links, VPN, cloud connections, and third-party connections.", "List critical data flows with source, destination, protocol, and encryption (cross-reference ID-REG-003).", "Record diagram version and date; update after every major network change."],
   ["แทรกแผนภาพเครือข่าย (เชิงตรรกะ) ที่แสดงโซน ไฟร์วอลล์ การเชื่อมต่ออินเทอร์เน็ต VPN การเชื่อมต่อคลาวด์ และการเชื่อมต่อกับบุคคลภายนอก", "ระบุการไหลของข้อมูลสำคัญพร้อมต้นทาง ปลายทาง โปรโตคอล และการเข้ารหัส (อ้างอิง ID-REG-003)", "บันทึกฉบับและวันที่ของแผนภาพ และปรับปรุงหลังการเปลี่ยนแปลงเครือข่ายที่สำคัญทุกครั้ง"],
   ["Diagram CMC-NET-2026-03 shows two hospitals linked by dual MPLS circuits, the primary data center at Riverside, DR site at Nonthaburi, and two internet providers.", "Critical flows: HIS to PACS and LIS through the interface engine (HL7 over TLS); modalities to PACS (DICOM, medical device VLAN); log forwarding to the MSSP (TLS).", "Updated March 2026 after the medical device VLAN project, phase 1."]),
 ],
 bp=[("Keep the diagram in a controlled repository and restrict access because it helps attackers.", "จัดเก็บแผนภาพในคลังเอกสารที่ควบคุม และจำกัดการเข้าถึง เพราะเป็นข้อมูลที่เป็นประโยชน์ต่อผู้โจมตี"),
     ("Validate the diagram against firewall rules and discovery scans each year.", "ตรวจสอบแผนภาพกับกฎไฟร์วอลล์และผลการสแกนค้นหาทุกปี")],
 mistakes=[("Diagrams that show the design from years ago, not today's network.", "แผนภาพแสดงการออกแบบเมื่อหลายปีก่อน ไม่ใช่เครือข่ายปัจจุบัน")],
)

C["ID-REG-004"] = dict(
 purpose=("This inventory records operational technology (OT) and medical devices that connect to the network, with their software, support status, and network placement, so their specific risks can be managed (ID.AM-01, ID.AM-02).",
          "ทะเบียนนี้บันทึกอุปกรณ์เทคโนโลยีปฏิบัติการ (OT) และอุปกรณ์การแพทย์ที่เชื่อมต่อเครือข่าย พร้อมซอฟต์แวร์ สถานะการสนับสนุน และตำแหน่งบนเครือข่าย เพื่อบริหารความเสี่ยงเฉพาะของอุปกรณ์เหล่านี้ (ID.AM-01, ID.AM-02)"),
 fields=[
  ("Device ID", "รหัสอุปกรณ์", "Unique tag.", "ป้ายรหัส", "MED-IMG-002"),
  ("Device type and manufacturer", "ประเภทและผู้ผลิต", "Function and maker.", "หน้าที่และผู้ผลิต", ""),
  ("Location and owner", "สถานที่และเจ้าของ", "Department.", "หน่วยงาน", ""),
  ("Embedded OS and version", "ระบบปฏิบัติการฝังตัวและรุ่น", "As reported by the manufacturer.", "ตามที่ผู้ผลิตระบุ", ""),
  ("Patch support", "การสนับสนุนแพตช์", "Manufacturer-certified patching available?", "ผู้ผลิตรับรองการติดตั้งแพตช์หรือไม่", ""),
  ("Network segment", "ส่วนเครือข่าย", "VLAN or zone.", "VLAN หรือโซน", ""),
  ("Remote vendor access", "การเข้าถึงระยะไกลของผู้ขาย", "Method.", "วิธีการ", ""),
  ("Clinical or safety criticality", "ความสำคัญด้านคลินิกหรือความปลอดภัย", "High, Medium, Low.", "สูง ปานกลาง ต่ำ", ""),
 ],
 rows=[
  ["MED-IMG-002", "CT scanner workstation, Vendor B partner", "Radiology, Riverside", "Windows 10 IoT Enterprise LTSC", "Quarterly certified patches", "VLAN 310 medical imaging", "Through CMC jump host", "High"],
  ["MED-LAB-011", "Chemistry analyzer, Vendor C partner", "Laboratory, Riverside", "Embedded Linux", "Manufacturer updates on site", "VLAN 320 laboratory devices", "None", "High"],
  ["MED-INF-GW1", "Infusion pump gateway", "Nursing, Riverside", "Windows Server 2016", "Annual", "VLAN 330 bedside devices", "Through CMC jump host", "High"],
  ["OT-BMS-01", "Building management system controller", "Facilities, Nonthaburi", "Vendor firmware", "On request", "VLAN 400 building systems", "Vendor VPN (to be replaced 2027)", "Medium"],
 ],
 bp=[("Use passive network discovery tools designed for medical and OT devices; active scans can disrupt them.", "ใช้เครื่องมือค้นหาเครือข่ายแบบ Passive ที่ออกแบบสำหรับอุปกรณ์การแพทย์และ OT เพราะการสแกนแบบ Active อาจรบกวนการทำงาน"),
     ("Obtain the Manufacturer Disclosure Statement for Medical Device Security (MDS2) form for each medical device model.", "ขอแบบฟอร์ม Manufacturer Disclosure Statement for Medical Device Security (MDS2) สำหรับอุปกรณ์การแพทย์แต่ละรุ่น"),
     ("Have biomedical engineering and IT co-own the inventory.", "ให้ฝ่ายวิศวกรรมชีวการแพทย์และฝ่าย IT เป็นเจ้าของทะเบียนร่วมกัน")],
 mistakes=[("Biomedical engineering tracks devices for maintenance only, with no network or software data.", "ฝ่ายวิศวกรรมชีวการแพทย์ติดตามอุปกรณ์เพื่อการบำรุงรักษาเท่านั้น โดยไม่มีข้อมูลเครือข่ายหรือซอฟต์แวร์")],
)

C["ID-RPT-002"] = dict(
 purpose=("The Business Impact Analysis (BIA) identifies critical business processes, the impact of their disruption over time, and the recovery objectives and resources they need (ID.AM-05, GV.OC-04, GV.OC-05).",
          "การวิเคราะห์ผลกระทบทางธุรกิจ (BIA) ระบุกระบวนการทางธุรกิจที่สำคัญ ผลกระทบของการหยุดชะงักตามช่วงเวลา และเป้าหมายการกู้คืนและทรัพยากรที่จำเป็น (ID.AM-05, GV.OC-04, GV.OC-05)"),
 sections=[
  ("Method", "วิธีการ", "Describe how impacts are assessed and objectives set (ISO 22301:2019 Clause 8.2.2).", "อธิบายวิธีประเมินผลกระทบและกำหนดเป้าหมาย (ISO 22301:2019 ข้อ 8.2.2)",
   ["Interview process owners using a standard questionnaire.", "Assess impact at 1 hour, 4 hours, 24 hours, 72 hours, and 1 week using the impact scale in GV-PRC-001.",
    "Set the maximum tolerable period of disruption (MTPD), recovery time objective (RTO), and recovery point objective (RPO) for each process.", "Identify dependencies: systems, data, people, suppliers, facilities.", "Validate results with the [ISSC]."],
   ["สัมภาษณ์เจ้าของกระบวนการด้วยแบบสอบถามมาตรฐาน", "ประเมินผลกระทบที่ 1 ชั่วโมง 4 ชั่วโมง 24 ชั่วโมง 72 ชั่วโมง และ 1 สัปดาห์ ด้วยมาตรวัดผลกระทบใน GV-PRC-001",
    "กำหนดระยะเวลาหยุดชะงักสูงสุดที่ยอมรับได้ (MTPD) เป้าหมายระยะเวลาการกู้คืน (RTO) และเป้าหมายจุดกู้คืนข้อมูล (RPO) ของแต่ละกระบวนการ", "ระบุการพึ่งพา ได้แก่ ระบบ ข้อมูล บุคลากร ผู้ให้บริการ และสถานที่", "ยืนยันผลกับ [ISSC]"]),
  ("BIA Results", "ผลการวิเคราะห์", "Record each critical process with impact, objectives, and dependencies.", "บันทึกกระบวนการสำคัญแต่ละรายการพร้อมผลกระทบ เป้าหมาย และการพึ่งพา",
   {"t": ["Process", "Impact at 4 hours", "MTPD", "RTO", "RPO", "Key dependencies"], "r": [["[Process]", "", "", "", "", ""], ["[Process]", "", "", "", "", ""]]},
   {"t": ["กระบวนการ", "ผลกระทบที่ 4 ชั่วโมง", "MTPD", "RTO", "RPO", "การพึ่งพาหลัก"], "r": [["[กระบวนการ]", "", "", "", "", ""], ["[กระบวนการ]", "", "", "", "", ""]]},
   {"t": ["Process", "Impact at 4 hours", "MTPD", "RTO", "RPO", "Key dependencies"], "r": [
     ["Emergency care", "Severe (patient safety)", "8 hours", "4 hours", "15 minutes", "HIS, network, Active Directory, LIS, PACS"],
     ["Inpatient medication administration", "Major", "8 hours", "4 hours", "15 minutes", "HIS pharmacy module, barcode scanners"],
     ["Diagnostic imaging", "Major", "24 hours", "8 hours", "1 hour", "PACS, modalities, Vendor B"],
     ["Laboratory testing", "Major", "24 hours", "8 hours", "1 hour", "LIS, analyzers, HL7 interface"],
     ["Billing and claims", "Moderate", "72 hours", "24 hours", "4 hours", "HIS billing, ERP, insurer portals"],
     ["Payroll", "Minor at 4 hours", "1 week", "72 hours", "24 hours", "ERP, bank file transfer"]]}),
 ],
 bp=[("Let process owners own the impact ratings; IT should not guess business impact.", "ให้เจ้าของกระบวนการเป็นผู้ประเมินระดับผลกระทบ ฝ่าย IT ไม่ควรคาดเดาผลกระทบทางธุรกิจเอง"),
     ("Compare RTO requirements with tested recovery capability and report the gap.", "เปรียบเทียบ RTO ที่ต้องการกับความสามารถในการกู้คืนที่ทดสอบแล้ว และรายงานช่องว่าง"),
     ("Refresh the BIA every year or after major business change.", "ปรับปรุง BIA ทุกปี หรือหลังการเปลี่ยนแปลงทางธุรกิจที่สำคัญ")],
 mistakes=[("Every process is rated critical with a 1-hour RTO, which no budget can support.", "ทุกกระบวนการถูกจัดเป็นระดับวิกฤตและมี RTO 1 ชั่วโมง ซึ่งไม่มีงบประมาณใดรองรับได้")],
)

C["ID-FRM-001"] = dict(
 purpose=("This record documents the sanitization or destruction of storage media and devices before disposal, reuse, or return, as evidence that data cannot be recovered.",
          "บันทึกนี้ใช้บันทึกการล้างหรือทำลายสื่อบันทึกข้อมูลและอุปกรณ์ก่อนจำหน่าย นำกลับมาใช้ใหม่ หรือส่งคืน เพื่อเป็นหลักฐานว่าไม่สามารถกู้คืนข้อมูลได้"),
 fields=[
  ("Record number", "เลขที่บันทึก", "Unique reference.", "รหัสอ้างอิง", "DSP-2026-001"),
  ("Asset ID and serial number", "รหัสทรัพย์สินและหมายเลขเครื่อง", "From inventory.", "จากทะเบียนทรัพย์สิน", ""),
  ("Media type", "ประเภทสื่อ", "HDD, SSD, tape, USB, mobile, embedded storage.", "HDD SSD เทป USB อุปกรณ์เคลื่อนที่ หน่วยความจำฝังตัว", ""),
  ("Highest data class", "ชั้นข้อมูลสูงสุด", "Per PR-STD-004.", "ตาม PR-STD-004", ""),
  ("Method (NIST SP 800-88)", "วิธีการ (NIST SP 800-88)", "Clear, Purge, or Destroy, with tool used.", "Clear Purge หรือ Destroy พร้อมเครื่องมือที่ใช้", ""),
  ("Performed by and date", "ผู้ดำเนินการและวันที่", "Name or vendor.", "ชื่อหรือผู้ให้บริการ", ""),
  ("Verification", "การยืนยันผล", "Verification method and result.", "วิธีการยืนยันและผล", ""),
  ("Certificate of destruction", "หนังสือรับรองการทำลาย", "Reference if external vendor.", "เลขอ้างอิงกรณีใช้ผู้ให้บริการภายนอก", ""),
  ("Inventory updated", "ปรับปรุงทะเบียนแล้ว", "Date.", "วันที่", ""),
 ],
 cmc_vals=["DSP-2026-044", "WS-OPD-118 / S/N 5CD0xxxxx", "SSD 256 GB", "Restricted (patient data)", "Purge: cryptographic erase using manufacturer tool, then physical destruction by vendor",
           "IT Service Desk technician; certified disposal vendor, 14 August 2026", "Tool report shows successful cryptographic erase", "COD-2026-0815", "15 August 2026"],
 approvals=["Reviewer", "ITM"],
 bp=[("Physically destroy SSDs that held Restricted data; overwriting is not reliable on flash media.", "ทำลาย SSD ที่เคยเก็บข้อมูลระดับ Restricted ทางกายภาพ เพราะการเขียนทับไม่น่าเชื่อถือสำหรับสื่อแบบ Flash")],
 mistakes=[("Disposal vendor collects devices without serial-number-level certificates.", "ผู้ให้บริการทำลายรับอุปกรณ์ไปโดยไม่มีหนังสือรับรองระดับหมายเลขเครื่อง")],
)
