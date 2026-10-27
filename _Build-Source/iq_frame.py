# -*- coding: utf-8 -*-
"""Scene-setting (f) and scenario question (x) for each CSF 2.0 Subcategory, written for interviewees who are not security specialists.
f = what to say before asking, in plain language. x = a concrete situation the interviewee can picture and answer. Pairs are (EN, TH)."""
F = {}
def fr(sid, f_en, f_th, x_en, x_th):
    F[sid] = dict(f=[f_en, f_th], x=[x_en, x_th])

# ---------- GV.OC ----------
fr("GV.OC-01",
   "Security budgets are limited, so we want to protect first what matters most to the business. That starts from your priorities, not from IT.",
   "งบด้านความมั่นคงปลอดภัยมีจำกัด จึงควรปกป้องสิ่งที่สำคัญต่อธุรกิจที่สุดก่อน และสิ่งนั้นต้องเริ่มจากลำดับความสำคัญของผู้บริหาร ไม่ใช่จากฝ่าย IT",
   "If all systems went down tomorrow morning and IT could restore only one by noon, which one would you choose, and why?",
   "หากพรุ่งนี้เช้าระบบทั้งหมดล่ม และ IT กู้คืนได้เพียงระบบเดียวภายในเที่ยง ท่านจะเลือกระบบใด และเพราะอะไร")
fr("GV.OC-02",
   "Customers, regulators, auditors, and partners increasingly ask how we protect data. Their expectations shape what we must do.",
   "ลูกค้า หน่วยงานกำกับ ผู้ตรวจสอบ และคู่ค้า สอบถามมากขึ้นเรื่อย ๆ ว่าองค์กรปกป้องข้อมูลอย่างไร ความคาดหวังเหล่านี้เป็นตัวกำหนดสิ่งที่องค์กรต้องทำ",
   "In the last year, did any customer, partner, or regulator ask for proof of your security? Who answered, and how long did it take?",
   "ในปีที่ผ่านมา มีลูกค้า คู่ค้า หรือหน่วยงานกำกับขอหลักฐานด้านความมั่นคงปลอดภัยหรือไม่ ใครเป็นผู้ตอบ และใช้เวลานานเท่าใด")
fr("GV.OC-03",
   "Several Thai laws now carry cybersecurity duties, such as the Cybersecurity Act and the PDPA. Missing one can lead to fines or orders from a regulator.",
   "ปัจจุบันกฎหมายไทยหลายฉบับมีหน้าที่ด้านไซเบอร์ เช่น พ.ร.บ.ไซเบอร์ และ PDPA หากพลาดไปข้อหนึ่งอาจถูกปรับหรือถูกสั่งการจากหน่วยงานกำกับ",
   "If a new regulator notification were published next month, who would notice it first, and how would it reach the people who must act?",
   "หากเดือนหน้ามีประกาศใหม่จากหน่วยงานกำกับ ใครจะรู้ก่อน และเรื่องจะไปถึงผู้ที่ต้องดำเนินการได้อย่างไร")
fr("GV.OC-04",
   "Customers and partners rely on some of our services every day. Knowing which ones, and how long they can wait, tells us where security must be strongest.",
   "ลูกค้าและคู่ค้าพึ่งพาบริการบางอย่างขององค์กรทุกวัน การรู้ว่าบริการใดและรอได้นานเท่าใด บอกได้ว่าความมั่นคงปลอดภัยต้องเข้มแข็งที่สุดตรงไหน",
   "If your main customer-facing service stopped for four hours, what would customers do, and what would it cost you?",
   "หากบริการหลักที่ให้ลูกค้าหยุดไป 4 ชั่วโมง ลูกค้าจะทำอย่างไร และองค์กรจะเสียหายเท่าใด")
fr("GV.OC-05",
   "We also depend on others: internet, cloud, software vendors, and key people. A failure on their side becomes our failure.",
   "องค์กรเองก็พึ่งพาผู้อื่น เช่น อินเทอร์เน็ต คลาวด์ ผู้ขายซอฟต์แวร์ และบุคลากรสำคัญ หากฝั่งเขาล้มเหลว ก็กลายเป็นความล้มเหลวขององค์กร",
   "If your main software vendor went out of business tomorrow, or your internet link was cut for a day, what would stop working?",
   "หากผู้ขายซอฟต์แวร์หลักเลิกกิจการพรุ่งนี้ หรืออินเทอร์เน็ตถูกตัดหนึ่งวัน อะไรจะใช้งานไม่ได้บ้าง")

# ---------- GV.RM ----------
fr("GV.RM-01",
   "Risk management needs a clear aim, for example \"no critical service down for more than four hours\". Without an aim, every risk looks equally urgent.",
   "การบริหารความเสี่ยงต้องมีเป้าหมายชัดเจน เช่น \"บริการสำคัญต้องไม่หยุดเกิน 4 ชั่วโมง\" หากไม่มีเป้าหมาย ทุกความเสี่ยงจะดูเร่งด่วนเท่ากันหมด",
   "If I asked three of your managers what cybersecurity must achieve this year, would they give me the same answer?",
   "หากถามผู้จัดการ 3 คนว่าปีนี้ด้านไซเบอร์ต้องบรรลุอะไร ทั้งสามคนจะตอบเหมือนกันหรือไม่")
fr("GV.RM-02",
   "Risk appetite is how much loss or disruption management can live with. It lets staff make decisions without asking you every time.",
   "ระดับความเสี่ยงที่ยอมรับได้คือความเสียหายหรือการหยุดชะงักที่ผู้บริหารรับได้ ช่วยให้พนักงานตัดสินใจได้เองโดยไม่ต้องถามผู้บริหารทุกครั้ง",
   "Would you accept losing one day of patient or customer data in exchange for a cheaper backup solution? Where is your limit?",
   "ท่านยอมรับการสูญเสียข้อมูลผู้รับบริการหรือลูกค้า 1 วัน เพื่อแลกกับระบบสำรองข้อมูลที่ถูกลงได้หรือไม่ ขีดจำกัดของท่านอยู่ที่ใด")
fr("GV.RM-03",
   "Most organizations already manage financial and operational risks in one register. Cyber risk should sit in the same place, judged by the same people.",
   "องค์กรส่วนใหญ่บริหารความเสี่ยงด้านการเงินและการดำเนินงานไว้ในทะเบียนเดียวอยู่แล้ว ความเสี่ยงไซเบอร์ควรอยู่ที่เดียวกันและพิจารณาโดยคนกลุ่มเดียวกัน",
   "At the last risk committee meeting, was ransomware or data leakage on the agenda next to other business risks?",
   "ในการประชุมคณะกรรมการความเสี่ยงครั้งล่าสุด แรนซัมแวร์หรือข้อมูลรั่วไหลอยู่ในวาระคู่กับความเสี่ยงธุรกิจอื่นหรือไม่")
fr("GV.RM-04",
   "For each risk there are four choices: reduce it, insure or outsource it, stop the activity, or accept it. Someone must have the authority to choose.",
   "ความเสี่ยงแต่ละเรื่องมีทางเลือก 4 ทาง คือ ลด โอนด้วยประกันหรือจ้างภายนอก เลิกทำกิจกรรมนั้น หรือยอมรับ และต้องมีผู้มีอำนาจตัดสินใจเลือก",
   "If IT said an old system cannot be secured and costs 5 million baht to replace, who would decide whether to replace it, insure it, or live with it?",
   "หาก IT แจ้งว่าระบบเก่าระบบหนึ่งทำให้ปลอดภัยไม่ได้ และต้องใช้งบ 5 ล้านบาทในการเปลี่ยน ใครจะตัดสินใจว่าจะเปลี่ยน ทำประกัน หรือยอมรับความเสี่ยง")
fr("GV.RM-05",
   "Bad news must travel fast. A risk found by a junior engineer is only useful if it reaches someone who can act.",
   "ข่าวร้ายต้องไปถึงเร็ว ความเสี่ยงที่วิศวกรระดับต้นพบจะมีประโยชน์ก็ต่อเมื่อไปถึงผู้ที่ตัดสินใจได้",
   "If a supplier told an IT staff member on Friday night that your data might be exposed, when would you personally hear about it?",
   "หากคืนวันศุกร์ผู้ให้บริการแจ้งเจ้าหน้าที่ IT ว่าข้อมูลขององค์กรอาจรั่วไหล ท่านจะทราบเรื่องเมื่อใด")
fr("GV.RM-06",
   "Risks must be rated the same way every time, otherwise the loudest person wins the budget.",
   "ความเสี่ยงต้องให้คะแนนด้วยวิธีเดียวกันทุกครั้ง มิฉะนั้นผู้ที่พูดเสียงดังที่สุดจะได้งบประมาณไป",
   "If two departments each claimed their security project was urgent, how would you compare them fairly?",
   "หากสองฝ่ายต่างอ้างว่าโครงการด้านความมั่นคงปลอดภัยของตนเร่งด่วน ท่านจะเปรียบเทียบอย่างเป็นธรรมได้อย่างไร")
fr("GV.RM-07",
   "Security is not only about loss. Good security can win customers, enable new digital services, or support a certification.",
   "ความมั่นคงปลอดภัยไม่ได้มีแค่เรื่องความเสียหาย ความมั่นคงปลอดภัยที่ดีช่วยให้ได้ลูกค้า เปิดบริการดิจิทัลใหม่ หรือสนับสนุนการได้รับการรับรอง",
   "Has a strong security record ever helped you win a contract or launch a new service? Do you discuss that upside when planning?",
   "เคยมีกรณีที่ความมั่นคงปลอดภัยที่ดีช่วยให้ได้สัญญาหรือเปิดบริการใหม่หรือไม่ และได้พิจารณาประโยชน์ด้านนี้ตอนวางแผนหรือไม่")

# ---------- GV.RR ----------
fr("GV.RR-01",
   "Regulators and courts now expect leadership, not only IT, to own cyber risk, the same way leadership owns financial risk. Staff follow what leaders pay attention to.",
   "ปัจจุบันหน่วยงานกำกับคาดหวังให้ผู้บริหาร ไม่ใช่แค่ IT เป็นเจ้าของความเสี่ยงไซเบอร์ เช่นเดียวกับความเสี่ยงทางการเงิน และพนักงานจะทำตามสิ่งที่ผู้บริหารให้ความสำคัญ",
   "Imagine a peer company was hit by ransomware last week and a journalist calls you. Who in your leadership team answers for cybersecurity, and when did the board last discuss it?",
   "สมมติสัปดาห์ที่แล้วบริษัทในธุรกิจเดียวกันโดนแรนซัมแวร์ แล้วนักข่าวโทรมาหาท่าน ใครในทีมผู้บริหารเป็นผู้รับผิดชอบเรื่องไซเบอร์ และคณะกรรมการพูดเรื่องนี้ครั้งล่าสุดเมื่อใด")
fr("GV.RR-02",
   "When everyone is a little responsible, no one is accountable. Each security task needs a named owner with the authority to act.",
   "เมื่อทุกคนรับผิดชอบนิดหน่อย จะไม่มีใครรับผิดชอบจริง งานด้านความมั่นคงปลอดภัยแต่ละเรื่องต้องมีเจ้าของที่ระบุชื่อและมีอำนาจดำเนินการ",
   "If a project manager wanted to launch a system next week without a security review, who could say no, and would that person be backed by management?",
   "หากผู้จัดการโครงการต้องการเปิดใช้ระบบสัปดาห์หน้าโดยไม่ผ่านการตรวจด้านความมั่นคงปลอดภัย ใครปฏิเสธได้ และผู้บริหารจะสนับสนุนคนนั้นหรือไม่")
fr("GV.RR-03",
   "Security spending should follow the size of the risk, not last year's budget plus five percent.",
   "งบด้านความมั่นคงปลอดภัยควรสัมพันธ์กับขนาดของความเสี่ยง ไม่ใช่งบปีที่แล้วบวกเพิ่มร้อยละ 5",
   "If your security lead asked for budget for one extra person next year, what would they need to show you to get a yes?",
   "หากหัวหน้าด้านความมั่นคงปลอดภัยของบเพิ่มคนหนึ่งตำแหน่งในปีหน้า เขาต้องแสดงอะไรให้ท่านเห็นจึงจะอนุมัติ")
fr("GV.RR-04",
   "Many incidents start with people: a new hire with too much access, or a leaver whose account still works. HR processes are a security control.",
   "เหตุการณ์จำนวนมากเริ่มจากเรื่องคน เช่น พนักงานใหม่ได้สิทธิ์มากเกินไป หรือพนักงานที่ลาออกแล้วแต่บัญชียังใช้ได้ กระบวนการ HR จึงเป็นการควบคุมด้านความมั่นคงปลอดภัยด้วย",
   "If a system administrator resigned angrily this afternoon, what would happen to their access before they left the building?",
   "หากผู้ดูแลระบบลาออกอย่างไม่พอใจบ่ายวันนี้ สิทธิ์การเข้าถึงของเขาจะถูกจัดการอย่างไรก่อนเขาออกจากอาคาร")

# ---------- GV.PO ----------
fr("GV.PO-01",
   "A policy is management's written instruction on security. Without it, staff cannot be held to a rule and auditors will find nothing to test.",
   "นโยบายคือคำสั่งที่เป็นลายลักษณ์อักษรของผู้บริหารเรื่องความมั่นคงปลอดภัย หากไม่มี ก็ไม่สามารถให้พนักงานถือปฏิบัติ และผู้ตรวจสอบก็ไม่มีอะไรให้ทดสอบ",
   "If an employee shared patient or customer data on a personal LINE group, which written rule would you point to when taking action?",
   "หากพนักงานส่งข้อมูลผู้รับบริการหรือลูกค้าในกลุ่ม LINE ส่วนตัว ท่านจะอ้างกฎข้อใดที่เป็นลายลักษณ์อักษรเมื่อดำเนินการ")
fr("GV.PO-02",
   "Technology, threats, and laws change every year. A policy written five years ago may not mention cloud, remote work, or AI.",
   "เทคโนโลยี ภัยคุกคาม และกฎหมายเปลี่ยนทุกปี นโยบายที่เขียนเมื่อ 5 ปีก่อนอาจไม่ได้พูดถึงคลาวด์ การทำงานจากที่บ้าน หรือ AI",
   "Does your current policy say anything about staff using ChatGPT or working from home? When did someone last check?",
   "นโยบายปัจจุบันพูดถึงการใช้ ChatGPT หรือการทำงานจากที่บ้านหรือไม่ และมีคนตรวจสอบครั้งล่าสุดเมื่อใด")

# ---------- GV.OV ----------
fr("GV.OV-01",
   "Strategy needs a feedback loop: management checks whether security work is producing the intended results and changes course if not.",
   "กลยุทธ์ต้องมีการติดตามผล ผู้บริหารต้องตรวจว่างานด้านความมั่นคงปลอดภัยให้ผลตามที่ตั้งใจหรือไม่ และปรับทิศทางเมื่อไม่เป็นไปตามเป้า",
   "Can you name one security decision management changed in the last year because results were not good enough?",
   "ระบุการตัดสินใจด้านความมั่นคงปลอดภัยหนึ่งเรื่องที่ผู้บริหารเปลี่ยนในปีที่ผ่านมาเพราะผลยังไม่ดีพอได้หรือไม่")
fr("GV.OV-02",
   "The threat picture changes, for example ransomware groups now target hospitals and factories. The strategy must be rechecked against new risks and new laws.",
   "ภาพของภัยคุกคามเปลี่ยนไป เช่น กลุ่มแรนซัมแวร์หันมาโจมตีโรงพยาบาลและโรงงาน กลยุทธ์จึงต้องตรวจทานใหม่เทียบกับความเสี่ยงและกฎหมายใหม่",
   "After the last major cyber attack in the news in Thailand, did anyone review whether the same thing could happen here?",
   "หลังเหตุโจมตีไซเบอร์ครั้งใหญ่ล่าสุดในไทยที่เป็นข่าว มีใครทบทวนหรือไม่ว่าเหตุการณ์แบบเดียวกันจะเกิดที่นี่ได้หรือไม่")
fr("GV.OV-03",
   "What gets measured gets managed. A few simple numbers show management whether security is improving.",
   "สิ่งที่วัดผลได้จึงจะบริหารได้ ตัวเลขง่าย ๆ ไม่กี่ตัวช่วยให้ผู้บริหารเห็นว่าความมั่นคงปลอดภัยดีขึ้นหรือไม่",
   "If I asked you today whether security is better than last year, what number or report would you look at?",
   "หากวันนี้ถามว่าความมั่นคงปลอดภัยดีกว่าปีที่แล้วหรือไม่ ท่านจะดูตัวเลขหรือรายงานใดเพื่อตอบ")

# ---------- GV.SC ----------
fr("GV.SC-01",
   "Many recent breaches came through a supplier: an IT vendor, a cloud service, or a maintenance company with remote access. Supplier risk needs its own rules.",
   "การละเมิดหลายครั้งในช่วงหลังเข้ามาทางผู้ให้บริการ เช่น ผู้ขาย IT บริการคลาวด์ หรือบริษัทบำรุงรักษาที่เข้าถึงจากระยะไกลได้ ความเสี่ยงจากผู้ให้บริการจึงต้องมีกติกาเฉพาะ",
   "If a vendor that maintains your core system were hacked, could the attacker reach your network? Who is responsible for checking that today?",
   "หากผู้ขายที่ดูแลระบบหลักขององค์กรถูกเจาะ ผู้โจมตีจะเข้าถึงเครือข่ายขององค์กรได้หรือไม่ และปัจจุบันใครรับผิดชอบตรวจสอบเรื่องนี้")
fr("GV.SC-02",
   "With outsourced and cloud services, it must be clear who does what. Gaps appear where each side assumes the other is responsible.",
   "เมื่อใช้บริการภายนอกหรือคลาวด์ ต้องชัดเจนว่าใครทำอะไร ช่องโหว่มักเกิดตรงที่แต่ละฝ่ายคิดว่าอีกฝ่ายรับผิดชอบ",
   "If data in your cloud service were deleted by mistake, would the provider restore it, or is that your job?",
   "หากข้อมูลในบริการคลาวด์ถูกลบโดยไม่ตั้งใจ ผู้ให้บริการจะกู้คืนให้ หรือเป็นหน้าที่ขององค์กรเอง")
fr("GV.SC-03",
   "Supplier risks should be judged alongside other business risks, not handled only by procurement.",
   "ความเสี่ยงจากผู้ให้บริการควรพิจารณาคู่กับความเสี่ยงธุรกิจอื่น ไม่ใช่ให้ฝ่ายจัดซื้อจัดการเพียงฝ่ายเดียว",
   "Is there any supplier you could not replace within a month? Is that dependency written down as a risk?",
   "มีผู้ให้บริการรายใดที่หากต้องเปลี่ยนจะทำไม่ได้ภายในหนึ่งเดือนหรือไม่ และการพึ่งพานี้ถูกบันทึกเป็นความเสี่ยงหรือไม่")
fr("GV.SC-04",
   "You cannot protect against suppliers you do not know about. A list ranked by importance tells you where to look first.",
   "องค์กรไม่สามารถป้องกันความเสี่ยงจากผู้ให้บริการที่ไม่รู้ว่ามีอยู่ รายชื่อที่จัดลำดับความสำคัญบอกได้ว่าควรดูที่ใดก่อน",
   "How many suppliers can connect to your systems remotely today? Could IT give me that list within an hour?",
   "ปัจจุบันมีผู้ให้บริการกี่รายที่เชื่อมต่อเข้าระบบจากระยะไกลได้ IT ส่งรายชื่อให้ได้ภายในหนึ่งชั่วโมงหรือไม่")
fr("GV.SC-05",
   "The contract is your strongest lever with a supplier. If security duties are not written in, you cannot enforce them after a breach.",
   "สัญญาคือเครื่องมือที่มีน้ำหนักที่สุดกับผู้ให้บริการ หากไม่ได้เขียนหน้าที่ด้านความมั่นคงปลอดภัยไว้ ก็บังคับไม่ได้เมื่อเกิดเหตุ",
   "If a supplier leaked your data, would the contract require them to tell you within a set time and pay for the damage?",
   "หากผู้ให้บริการทำข้อมูลขององค์กรรั่วไหล สัญญากำหนดให้ต้องแจ้งภายในเวลาที่กำหนดและชดใช้ความเสียหายหรือไม่")
fr("GV.SC-06",
   "It is much easier to check a supplier before signing than to fix problems after.",
   "การตรวจสอบผู้ให้บริการก่อนลงนามทำได้ง่ายกว่าการแก้ปัญหาภายหลังมาก",
   "When you bought your last major system, did anyone ask the vendor how they protect your data before the contract was signed?",
   "ตอนจัดซื้อระบบใหญ่ครั้งล่าสุด มีใครถามผู้ขายหรือไม่ว่าเขาปกป้องข้อมูลขององค์กรอย่างไร ก่อนลงนามสัญญา")
fr("GV.SC-07",
   "A supplier that was safe three years ago may not be safe today. Critical suppliers need periodic checks.",
   "ผู้ให้บริการที่ปลอดภัยเมื่อ 3 ปีก่อนอาจไม่ปลอดภัยในวันนี้ ผู้ให้บริการสำคัญจึงต้องได้รับการตรวจตามรอบ",
   "When did anyone last review how your most critical supplier handles security?",
   "มีการทบทวนครั้งล่าสุดเมื่อใดว่าผู้ให้บริการที่สำคัญที่สุดจัดการความมั่นคงปลอดภัยอย่างไร")
fr("GV.SC-08",
   "During an incident you may need a supplier's help at 2 a.m. That only works if it was agreed and practiced in advance.",
   "ระหว่างเกิดเหตุ องค์กรอาจต้องการความช่วยเหลือจากผู้ให้บริการตอนตีสอง ซึ่งจะได้ผลก็ต่อเมื่อตกลงและซ้อมไว้ล่วงหน้า",
   "If your core system were encrypted by ransomware on a Sunday night, who at the vendor would you call, and would they answer?",
   "หากระบบหลักถูกแรนซัมแวร์เข้ารหัสคืนวันอาทิตย์ ท่านจะโทรหาใครที่ผู้ขาย และเขาจะรับสายหรือไม่")
fr("GV.SC-09",
   "Security commitments from suppliers must be checked through the whole life of the product or service, including updates and support.",
   "คำมั่นด้านความมั่นคงปลอดภัยของผู้ให้บริการต้องได้รับการตรวจตลอดอายุของผลิตภัณฑ์หรือบริการ รวมถึงการอัปเดตและการสนับสนุน",
   "Do you know when your key vendors will stop providing security updates for the products you use?",
   "ทราบหรือไม่ว่าผู้ขายหลักจะหยุดให้อัปเดตด้านความมั่นคงปลอดภัยสำหรับผลิตภัณฑ์ที่องค์กรใช้เมื่อใด")
fr("GV.SC-10",
   "When a contract ends, old accounts and copies of data often stay behind. Exit steps prevent that.",
   "เมื่อสัญญาสิ้นสุด บัญชีเก่าและสำเนาข้อมูลมักยังค้างอยู่ ขั้นตอนการยุติช่วยป้องกันปัญหานี้",
   "Think of the last vendor you stopped using. Can you be sure their accounts are disabled and your data is deleted?",
   "นึกถึงผู้ขายรายล่าสุดที่เลิกใช้บริการ มั่นใจได้หรือไม่ว่าบัญชีของเขาถูกระงับและข้อมูลขององค์กรถูกลบแล้ว")

# ---------- ID.AM ----------
fr("ID.AM-01",
   "Attackers look for the forgotten computer in the corner. You can only protect devices you know you have.",
   "ผู้โจมตีมักมองหาคอมพิวเตอร์ที่ถูกลืมไว้ ปกป้องได้เฉพาะอุปกรณ์ที่รู้ว่ามีอยู่",
   "If I walked into your server room or a ward and picked a random device, could IT tell me who owns it and whether it is patched?",
   "หากผมเดินเข้าห้องเซิร์ฟเวอร์หรือแผนกหนึ่งแล้วชี้อุปกรณ์สุ่มหนึ่งเครื่อง IT บอกได้หรือไม่ว่าใครเป็นเจ้าของและอัปเดตแล้วหรือยัง")
fr("ID.AM-02",
   "Every application and cloud service holds data and needs updates. Software bought by departments without IT is a common blind spot.",
   "ทุกระบบงานและบริการคลาวด์มีข้อมูลและต้องอัปเดต ซอฟต์แวร์ที่หน่วยงานซื้อเองโดยไม่ผ่าน IT เป็นจุดบอดที่พบบ่อย",
   "If a department signed up for an online tool with a company credit card, would IT ever find out?",
   "หากหน่วยงานหนึ่งสมัครใช้เครื่องมือออนไลน์ด้วยบัตรเครดิตบริษัท IT จะรู้หรือไม่")
fr("ID.AM-03",
   "A network map shows how data moves and where an attacker could travel. Without it, response during an incident is guesswork.",
   "แผนผังเครือข่ายแสดงว่าข้อมูลไหลอย่างไรและผู้โจมตีจะเคลื่อนที่ไปได้ทางใด หากไม่มี การรับมือเหตุการณ์ก็เป็นการเดา",
   "If an infected computer were found in the finance department, could IT quickly show which other systems it can reach?",
   "หากพบคอมพิวเตอร์ติดมัลแวร์ในฝ่ายการเงิน IT แสดงได้เร็วหรือไม่ว่าเครื่องนั้นเข้าถึงระบบอื่นใดได้บ้าง")
fr("ID.AM-04",
   "Outsourced services are part of your environment too. A list of them shows what you depend on outside your walls.",
   "บริการที่จ้างภายนอกก็เป็นส่วนหนึ่งของสภาพแวดล้อมขององค์กร รายการบริการเหล่านี้แสดงสิ่งที่องค์กรพึ่งพาจากภายนอก",
   "If a cloud provider announced a breach, how fast could you tell whether you use that provider and for what?",
   "หากผู้ให้บริการคลาวด์รายหนึ่งประกาศว่าถูกเจาะ องค์กรรู้ได้เร็วเพียงใดว่าใช้ผู้ให้บริการรายนั้นหรือไม่และใช้ทำอะไร")
fr("ID.AM-05",
   "Not every system deserves the same protection. Ranking systems by business impact lets you spend where it matters.",
   "ไม่ใช่ทุกระบบที่ต้องการการปกป้องระดับเดียวกัน การจัดลำดับระบบตามผลกระทบทางธุรกิจช่วยให้ใช้งบตรงจุด",
   "If you had budget to fully protect only five systems, which five, and does IT agree with your list?",
   "หากมีงบปกป้องเต็มที่ได้เพียง 5 ระบบ ท่านจะเลือกระบบใด และ IT เห็นตรงกับท่านหรือไม่")
fr("ID.AM-07",
   "Sensitive data such as health, ID card, or payroll records attracts attackers and regulators. You need to know where it lives.",
   "ข้อมูลอ่อนไหว เช่น ข้อมูลสุขภาพ เลขบัตรประชาชน หรือเงินเดือน เป็นเป้าหมายของผู้โจมตีและเป็นจุดที่หน่วยงานกำกับสนใจ องค์กรต้องรู้ว่าข้อมูลอยู่ที่ใด",
   "If a regulator asked where all copies of patient or customer ID card data are stored, including Excel files and email, could you answer?",
   "หากหน่วยงานกำกับถามว่าสำเนาข้อมูลบัตรประชาชนของผู้รับบริการหรือลูกค้าอยู่ที่ใดบ้าง รวมถึงไฟล์ Excel และอีเมล องค์กรตอบได้หรือไม่")
fr("ID.AM-08",
   "Old equipment and unsupported systems are easy targets, and discarded disks often still hold data.",
   "อุปกรณ์เก่าและระบบที่หมดการสนับสนุนเป็นเป้าหมายง่าย และดิสก์ที่ทิ้งแล้วมักยังมีข้อมูลอยู่",
   "When you replace old computers, where do the hard disks go, and who confirms the data is gone?",
   "เมื่อเปลี่ยนคอมพิวเตอร์เก่า ฮาร์ดดิสก์ไปอยู่ที่ใด และใครยืนยันว่าข้อมูลถูกลบแล้ว")

# ---------- ID.RA ----------
fr("ID.RA-01",
   "Every system has weaknesses. The question is whether you find them before attackers do.",
   "ทุกระบบมีจุดอ่อน คำถามคือองค์กรพบก่อนผู้โจมตีหรือไม่",
   "If a well-known vulnerability were announced today, how would you find out which of your systems are affected?",
   "หากวันนี้มีการประกาศช่องโหว่ร้ายแรงที่เป็นที่รู้จัก องค์กรจะรู้ได้อย่างไรว่าระบบใดบ้างได้รับผลกระทบ")
fr("ID.RA-02",
   "Threat intelligence is early warning from others: government CERTs, industry groups, and vendors. It gives you time to prepare.",
   "ข้อมูลข่าวกรองภัยคุกคามคือการเตือนล่วงหน้าจากผู้อื่น เช่น ศูนย์ CERT ภาครัฐ กลุ่มอุตสาหกรรม และผู้ขาย ช่วยให้มีเวลาเตรียมตัว",
   "When ThaiCERT or the NCSA publishes a warning about an active attack, who in your organization receives it and acts on it?",
   "เมื่อ ThaiCERT หรือ สกมช. ออกประกาศเตือนการโจมตีที่กำลังเกิดขึ้น ใครในองค์กรได้รับและนำไปดำเนินการ")
fr("ID.RA-03",
   "Different organizations face different attackers: criminals after money, insiders, or hacktivists. Knowing yours shapes your defenses.",
   "แต่ละองค์กรเผชิญผู้โจมตีต่างกัน เช่น อาชญากรที่ต้องการเงิน บุคคลภายใน หรือกลุ่มแฮกเกอร์ที่มีแรงจูงใจทางอุดมการณ์ การรู้ว่าองค์กรเผชิญกลุ่มใดช่วยกำหนดการป้องกัน",
   "Who would most want to attack your organization, and what would they be after?",
   "ใครน่าจะอยากโจมตีองค์กรของท่านมากที่สุด และเขาต้องการอะไร")
fr("ID.RA-04",
   "Risk is how likely something is to happen and how bad it would be. Business owners know the impact better than IT.",
   "ความเสี่ยงคือโอกาสที่จะเกิดและความรุนแรงหากเกิด เจ้าของกระบวนการธุรกิจรู้ผลกระทบดีกว่า IT",
   "If your billing system were unavailable for a week, how would you estimate the loss? Has anyone asked you that before?",
   "หากระบบเรียกเก็บเงินใช้งานไม่ได้หนึ่งสัปดาห์ ท่านจะประเมินความเสียหายอย่างไร และเคยมีใครถามท่านเรื่องนี้มาก่อนหรือไม่")
fr("ID.RA-05",
   "Combining threats, weaknesses, likelihood, and impact gives a ranked list of risks. That list should drive the security plan.",
   "การนำภัยคุกคาม จุดอ่อน โอกาส และผลกระทบมารวมกัน จะได้รายการความเสี่ยงที่จัดลำดับแล้ว และรายการนี้ควรเป็นตัวขับเคลื่อนแผนด้านความมั่นคงปลอดภัย",
   "What are your top three cyber risks today, and do the current security projects address them?",
   "ความเสี่ยงไซเบอร์ 3 อันดับแรกในวันนี้คืออะไร และโครงการด้านความมั่นคงปลอดภัยปัจจุบันตอบโจทย์ความเสี่ยงเหล่านั้นหรือไม่")
fr("ID.RA-06",
   "A risk register is only useful if each risk has an action, an owner, and a date, and someone follows up.",
   "ทะเบียนความเสี่ยงจะมีประโยชน์ก็ต่อเมื่อความเสี่ยงแต่ละเรื่องมีการดำเนินการ เจ้าของ วันที่ และมีคนติดตาม",
   "Pick one high risk from last year's assessment. What was done about it, and who checked that it was done?",
   "เลือกความเสี่ยงสูงหนึ่งเรื่องจากการประเมินปีที่แล้ว มีการดำเนินการอะไร และใครตรวจว่าทำแล้ว")
fr("ID.RA-07",
   "Many outages and breaches follow an unreviewed change. Exceptions to rules should be temporary and visible.",
   "เหตุระบบล่มและการละเมิดจำนวนมากเกิดหลังการเปลี่ยนแปลงที่ไม่ได้ทบทวน การยกเว้นกฎควรเป็นการชั่วคราวและมองเห็นได้",
   "If a vendor asked to open a firewall port 'just for a week', who would approve it, and who would close it afterwards?",
   "หากผู้ขายขอเปิดพอร์ตไฟร์วอลล์ 'แค่หนึ่งสัปดาห์' ใครเป็นผู้อนุมัติ และใครเป็นผู้ปิดหลังจากนั้น")
fr("ID.RA-08",
   "Sometimes outsiders find your weaknesses first. A simple reporting channel turns that into a warning instead of a headline.",
   "บางครั้งบุคคลภายนอกพบจุดอ่อนขององค์กรก่อน ช่องทางรับแจ้งง่าย ๆ ช่วยเปลี่ยนเรื่องนั้นเป็นการเตือนแทนที่จะเป็นข่าว",
   "If a university student found a flaw in your website and wanted to report it politely, where would they send it?",
   "หากนักศึกษาพบช่องโหว่ในเว็บไซต์และต้องการแจ้งอย่างสุภาพ เขาจะส่งเรื่องไปที่ใด")
fr("ID.RA-09",
   "Fake or tampered hardware and software can carry hidden malware. Buying from trusted sources reduces that risk.",
   "ฮาร์ดแวร์และซอฟต์แวร์ปลอมหรือที่ถูกดัดแปลงอาจมีมัลแวร์ซ่อนอยู่ การซื้อจากแหล่งที่เชื่อถือได้ช่วยลดความเสี่ยงนี้",
   "If a staff member found a cheaper network switch on an online marketplace, could they buy and install it?",
   "หากพนักงานพบสวิตช์เครือข่ายราคาถูกกว่าในตลาดออนไลน์ เขาสามารถซื้อมาติดตั้งเองได้หรือไม่")
fr("ID.RA-10",
   "Critical suppliers should pass a security check before you depend on them, just as you check their financial health.",
   "ผู้ให้บริการสำคัญควรผ่านการตรวจด้านความมั่นคงปลอดภัยก่อนที่องค์กรจะพึ่งพา เช่นเดียวกับการตรวจฐานะการเงิน",
   "For your newest critical supplier, what security information did you see before choosing them?",
   "สำหรับผู้ให้บริการสำคัญรายล่าสุด ท่านเห็นข้อมูลด้านความมั่นคงปลอดภัยอะไรก่อนเลือกเขา")

# ---------- ID.IM ----------
fr("ID.IM-01",
   "Audits and assessments only help if their findings are fixed. Open findings that repeat each year are a warning sign.",
   "การตรวจสอบและการประเมินจะมีประโยชน์ก็ต่อเมื่อข้อตรวจพบได้รับการแก้ไข ข้อตรวจพบที่ค้างและซ้ำทุกปีเป็นสัญญาณเตือน",
   "Are there audit findings that appeared both last year and this year? Why were they not closed?",
   "มีข้อตรวจพบที่ปรากฏทั้งปีที่แล้วและปีนี้หรือไม่ และทำไมยังไม่ถูกปิด")
fr("ID.IM-02",
   "Tests and drills show weaknesses safely. The value comes from what you change afterwards.",
   "การทดสอบและการฝึกซ้อมช่วยแสดงจุดอ่อนอย่างปลอดภัย คุณค่าอยู่ที่สิ่งที่เปลี่ยนแปลงหลังจากนั้น",
   "After your last fire drill or IT drill, what did you change because of what you learned?",
   "หลังการซ้อมอพยพหรือซ้อมด้าน IT ครั้งล่าสุด ท่านเปลี่ยนอะไรบ้างจากสิ่งที่ได้เรียนรู้")
fr("ID.IM-03",
   "Daily operations and small incidents reveal recurring problems. Fixing root causes prevents the next big incident.",
   "การทำงานประจำวันและเหตุการณ์เล็ก ๆ แสดงให้เห็นปัญหาที่เกิดซ้ำ การแก้ที่ต้นเหตุช่วยป้องกันเหตุการณ์ใหญ่ครั้งถัดไป",
   "Is there an IT problem that keeps coming back every few months? Has anyone looked for the root cause?",
   "มีปัญหา IT ที่กลับมาเกิดซ้ำทุกไม่กี่เดือนหรือไม่ และมีใครหาสาเหตุที่แท้จริงหรือไม่")
fr("ID.IM-04",
   "Plans for incidents and outages must be current and known to staff. An old plan in a drawer will not help at 3 a.m.",
   "แผนรับมือเหตุการณ์และเหตุขัดข้องต้องเป็นปัจจุบันและพนักงานรู้จัก แผนเก่าที่เก็บไว้ในลิ้นชักช่วยอะไรไม่ได้ตอนตีสาม",
   "If the network went down right now, where would staff find the incident plan, given the plan itself may be on the network?",
   "หากเครือข่ายล่มตอนนี้ พนักงานจะหาแผนรับมือเหตุการณ์ได้ที่ไหน ในเมื่อตัวแผนเองอาจอยู่บนเครือข่าย")

# ---------- PR.AA ----------
fr("PR.AA-01",
   "Every person, system, and device that logs in needs its own account, created and removed through a controlled process.",
   "ทุกคน ทุกระบบ และทุกอุปกรณ์ที่เข้าสู่ระบบต้องมีบัญชีของตนเอง และสร้างหรือลบผ่านกระบวนการที่ควบคุมได้",
   "If someone resigned last Friday, would their email and system accounts still work today?",
   "หากมีพนักงานลาออกเมื่อวันศุกร์ที่แล้ว วันนี้อีเมลและบัญชีระบบของเขายังใช้ได้อยู่หรือไม่")
fr("PR.AA-02",
   "Attackers often call the help desk pretending to be staff. Checking identity before issuing or resetting access stops this.",
   "ผู้โจมตีมักโทรหา Help Desk โดยแอบอ้างเป็นพนักงาน การยืนยันตัวตนก่อนออกหรือรีเซ็ตสิทธิ์ช่วยป้องกันได้",
   "If someone phoned the help desk claiming to be you and asked for a password reset, what would the help desk ask before doing it?",
   "หากมีคนโทรหา Help Desk อ้างว่าเป็นท่านและขอรีเซ็ตรหัสผ่าน Help Desk จะถามอะไรก่อนดำเนินการ")
fr("PR.AA-03",
   "Passwords are stolen every day. A second step, such as a code on your phone, blocks most account takeovers.",
   "รหัสผ่านถูกขโมยทุกวัน การยืนยันขั้นที่สอง เช่น รหัสในโทรศัพท์ ช่วยหยุดการยึดบัญชีได้เกือบทั้งหมด",
   "If your email password appeared on a hacker forum tonight, what would stop someone from logging in as you?",
   "หากคืนนี้รหัสผ่านอีเมลของท่านไปปรากฏในฟอรัมแฮกเกอร์ อะไรจะหยุดไม่ให้คนอื่นเข้าสู่ระบบในนามท่านได้")
fr("PR.AA-04",
   "Single sign-on lets staff log in once for many systems. The tokens behind it must be protected, or one theft opens every door.",
   "การลงชื่อเข้าใช้ครั้งเดียว (SSO) ช่วยให้พนักงานเข้าสู่ระบบครั้งเดียวแล้วใช้ได้หลายระบบ โทเคนเบื้องหลังต้องได้รับการปกป้อง มิฉะนั้นการขโมยครั้งเดียวจะเปิดได้ทุกประตู",
   "How many separate passwords does a typical employee need each day? Which systems still have their own login?",
   "พนักงานทั่วไปต้องใช้รหัสผ่านแยกกันกี่ชุดต่อวัน และระบบใดยังมีการเข้าสู่ระบบแยกของตัวเอง")
fr("PR.AA-05",
   "People should have only the access their job needs. Access grows over time as people change roles, so it must be reviewed.",
   "บุคลากรควรมีสิทธิ์เท่าที่งานต้องใช้ สิทธิ์มักเพิ่มขึ้นเรื่อย ๆ เมื่อคนย้ายตำแหน่ง จึงต้องทบทวนอยู่เสมอ",
   "If a nurse or clerk moved to a new department, would they keep access to the old department's data?",
   "หากพยาบาลหรือเจ้าหน้าที่ย้ายไปแผนกใหม่ เขายังเข้าถึงข้อมูลของแผนกเดิมได้อยู่หรือไม่")
fr("PR.AA-06",
   "Physical access is the easiest way around technical controls. Anyone who reaches a server can bypass many protections.",
   "การเข้าถึงทางกายภาพเป็นวิธีที่ง่ายที่สุดในการเลี่ยงการควบคุมทางเทคนิค ใครเข้าถึงเซิร์ฟเวอร์ได้ก็ข้ามการป้องกันได้หลายอย่าง",
   "Could a contractor in a uniform walk into your server room today without anyone stopping them?",
   "วันนี้ผู้รับเหมาที่ใส่เครื่องแบบเดินเข้าห้องเซิร์ฟเวอร์ได้โดยไม่มีใครหยุดหรือไม่")

# ---------- PR.AT ----------
fr("PR.AT-01",
   "Most attacks start with a staff member clicking a link or opening a file. Training turns staff into the first line of defense.",
   "การโจมตีส่วนใหญ่เริ่มจากพนักงานคลิกลิงก์หรือเปิดไฟล์ การอบรมช่วยให้พนักงานเป็นด่านแรกของการป้องกัน",
   "If an employee received a fake email from 'the CEO' asking for an urgent transfer, would they know what to do and whom to tell?",
   "หากพนักงานได้รับอีเมลปลอมจาก 'CEO' ขอให้โอนเงินด่วน เขาจะรู้หรือไม่ว่าต้องทำอย่างไรและแจ้งใคร")
fr("PR.AT-02",
   "Administrators, developers, and executives face targeted attacks and hold more power, so they need training for their role.",
   "ผู้ดูแลระบบ นักพัฒนา และผู้บริหาร เผชิญการโจมตีแบบเจาะจงและมีอำนาจมากกว่า จึงต้องได้รับการอบรมตามบทบาท",
   "When did your IT administrators last receive security training specific to their work, not the general staff course?",
   "ผู้ดูแลระบบ IT ได้รับการอบรมด้านความมั่นคงปลอดภัยเฉพาะงานของตน ไม่ใช่หลักสูตรพนักงานทั่วไป ครั้งล่าสุดเมื่อใด")

# ---------- PR.DS ----------
fr("PR.DS-01",
   "Stored data, on laptops, servers, or USB drives, should be unreadable to anyone who steals the device.",
   "ข้อมูลที่จัดเก็บ ไม่ว่าในโน้ตบุ๊ก เซิร์ฟเวอร์ หรือ USB ควรอ่านไม่ได้สำหรับผู้ที่ขโมยอุปกรณ์ไป",
   "If a manager's laptop were stolen from a car tonight, could the thief read the files on it?",
   "หากโน้ตบุ๊กของผู้จัดการถูกขโมยจากรถคืนนี้ ผู้ขโมยจะอ่านไฟล์ในเครื่องได้หรือไม่")
fr("PR.DS-02",
   "Data sent over networks or email can be intercepted. Encryption keeps it private on the way.",
   "ข้อมูลที่ส่งผ่านเครือข่ายหรืออีเมลอาจถูกดักได้ การเข้ารหัสช่วยรักษาความลับระหว่างทาง",
   "When staff send a file of patient or customer records to an outside partner, how do they send it today?",
   "เมื่อพนักงานส่งไฟล์ข้อมูลผู้รับบริการหรือลูกค้าให้คู่ค้าภายนอก ปัจจุบันส่งด้วยวิธีใด")
fr("PR.DS-10",
   "Data on screen or in use can be seen or copied. Screen locks and masking reduce casual exposure.",
   "ข้อมูลบนหน้าจอหรือที่กำลังใช้งานอาจถูกมองเห็นหรือคัดลอก การล็อกหน้าจอและการปิดบังข้อมูลช่วยลดการเปิดเผยโดยไม่ตั้งใจ",
   "If a staff member left their desk with a patient or customer record open, how long until the screen locks?",
   "หากพนักงานลุกจากโต๊ะโดยเปิดข้อมูลผู้รับบริการหรือลูกค้าทิ้งไว้ หน้าจอจะล็อกภายในเวลาเท่าใด")
fr("PR.DS-11",
   "Backups are the last line of defense against ransomware. Attackers now try to delete backups first, so backups must be protected and tested.",
   "ข้อมูลสำรองเป็นด่านสุดท้ายในการรับมือแรนซัมแวร์ ปัจจุบันผู้โจมตีพยายามลบข้อมูลสำรองก่อน จึงต้องปกป้องและทดสอบข้อมูลสำรอง",
   "If ransomware encrypted every server tonight, including the backup server, how many days of data would you lose, and how long would it take to be back?",
   "หากคืนนี้แรนซัมแวร์เข้ารหัสทุกเซิร์ฟเวอร์ รวมถึงเซิร์ฟเวอร์สำรองข้อมูล องค์กรจะสูญเสียข้อมูลกี่วัน และต้องใช้เวลานานเท่าใดจึงกลับมาใช้งานได้")

# ---------- PR.PS ----------
fr("PR.PS-01",
   "Systems come with insecure default settings. A standard secure setup, applied everywhere, closes many easy doors.",
   "ระบบมักมาพร้อมการตั้งค่าเริ่มต้นที่ไม่ปลอดภัย การตั้งค่ามาตรฐานที่ปลอดภัยและใช้ทุกเครื่องช่วยปิดช่องทางง่าย ๆ ได้มาก",
   "If IT set up a new server today, would it follow a written secure checklist, or depend on who installs it?",
   "หากวันนี้ IT ติดตั้งเซิร์ฟเวอร์ใหม่ จะทำตามรายการตรวจสอบที่ปลอดภัยเป็นลายลักษณ์อักษร หรือขึ้นกับว่าใครเป็นผู้ติดตั้ง")
fr("PR.PS-02",
   "Most attacks use weaknesses that already have a fix available. Timely updates close them.",
   "การโจมตีส่วนใหญ่ใช้จุดอ่อนที่มีแพตช์แก้ไขแล้ว การอัปเดตตามเวลาช่วยปิดจุดอ่อนเหล่านั้น",
   "If Microsoft released an urgent security fix today, how many days until all your servers had it?",
   "หากวันนี้ Microsoft ออกแพตช์ด่วนด้านความมั่นคงปลอดภัย ต้องใช้กี่วันจึงจะติดตั้งครบทุกเซิร์ฟเวอร์")
fr("PR.PS-03",
   "Old hardware fails more often and may no longer get security fixes.",
   "ฮาร์ดแวร์เก่าเสียบ่อยกว่าและอาจไม่ได้รับแพตช์ด้านความมั่นคงปลอดภัยแล้ว",
   "Which of your key network devices or servers are past their vendor support date?",
   "อุปกรณ์เครือข่ายหรือเซิร์ฟเวอร์หลักตัวใดที่หมดระยะการสนับสนุนจากผู้ขายแล้ว")
fr("PR.PS-04",
   "Logs are the security camera footage of IT. Without them, you cannot tell what happened during an incident.",
   "บันทึก (Log) เปรียบเหมือนภาพจากกล้องวงจรปิดของ IT หากไม่มี จะไม่รู้ว่าเกิดอะไรขึ้นระหว่างเหตุการณ์",
   "If you discovered that someone accessed payroll data last month, could IT tell you who it was and from where?",
   "หากพบว่ามีคนเข้าถึงข้อมูลเงินเดือนเมื่อเดือนที่แล้ว IT บอกได้หรือไม่ว่าเป็นใครและเข้าจากที่ใด")
fr("PR.PS-05",
   "Unapproved software is a common way malware gets in. Limiting who can install software blocks much of it.",
   "ซอฟต์แวร์ที่ไม่ได้รับอนุญาตเป็นช่องทางที่มัลแวร์เข้ามาบ่อย การจำกัดผู้ที่ติดตั้งซอฟต์แวร์ได้ช่วยป้องกันได้มาก",
   "If an employee downloaded a free PDF converter from the internet, could they install it on their work computer?",
   "หากพนักงานดาวน์โหลดโปรแกรมแปลงไฟล์ PDF ฟรีจากอินเทอร์เน็ต เขาติดตั้งบนคอมพิวเตอร์ที่ทำงานได้หรือไม่")
fr("PR.PS-06",
   "Software built in-house or by contractors can carry security flaws. Checking early is cheaper than fixing after launch.",
   "ซอฟต์แวร์ที่พัฒนาเองหรือจ้างพัฒนาอาจมีจุดอ่อนด้านความมั่นคงปลอดภัย การตรวจตั้งแต่แรกถูกกว่าการแก้หลังเปิดใช้",
   "Before your last application went live, did anyone test it for security, or only check that it worked?",
   "ก่อนเปิดใช้ระบบงานครั้งล่าสุด มีใครทดสอบด้านความมั่นคงปลอดภัยหรือไม่ หรือตรวจเพียงว่าใช้งานได้")

# ---------- PR.IR ----------
fr("PR.IR-01",
   "A flat network lets an attacker move from one infected computer to every system. Separating the network contains the damage.",
   "เครือข่ายที่ไม่แบ่งส่วนทำให้ผู้โจมตีเคลื่อนจากเครื่องที่ติดมัลแวร์หนึ่งเครื่องไปถึงทุกระบบได้ การแบ่งส่วนเครือข่ายช่วยจำกัดความเสียหาย",
   "If a guest Wi-Fi user or a medical device were infected, could it reach your main database servers?",
   "หากผู้ใช้ Wi-Fi สำหรับผู้มาติดต่อหรืออุปกรณ์การแพทย์ติดมัลแวร์ จะเข้าถึงเซิร์ฟเวอร์ฐานข้อมูลหลักได้หรือไม่")
fr("PR.IR-02",
   "Fire, flood, heat, and power loss can take down IT as surely as hackers.",
   "ไฟไหม้ น้ำท่วม ความร้อน และไฟฟ้าดับ ทำให้ระบบ IT ล่มได้ไม่ต่างจากแฮกเกอร์",
   "If the air conditioning in the server room failed on a Saturday night, who would know, and how fast?",
   "หากเครื่องปรับอากาศในห้องเซิร์ฟเวอร์เสียคืนวันเสาร์ ใครจะรู้ และรู้เร็วเพียงใด")
fr("PR.IR-03",
   "Critical services need a backup path: a second server, a second site, or a manual workaround, so one failure does not stop the business.",
   "บริการสำคัญต้องมีทางสำรอง เช่น เซิร์ฟเวอร์ที่สอง ศูนย์สำรอง หรือวิธีทำงานด้วยมือ เพื่อไม่ให้ความล้มเหลวจุดเดียวหยุดธุรกิจ",
   "If your main data center were unusable for three days, where would your critical systems run?",
   "หากศูนย์ข้อมูลหลักใช้งานไม่ได้ 3 วัน ระบบสำคัญจะทำงานที่ใด")
fr("PR.IR-04",
   "Systems slow down or stop when storage, processing, or bandwidth runs out. Monitoring capacity prevents surprise outages.",
   "ระบบจะช้าหรือหยุดเมื่อพื้นที่จัดเก็บ การประมวลผล หรือแบนด์วิดท์ไม่พอ การเฝ้าระวังขีดความสามารถช่วยป้องกันระบบล่มแบบไม่คาดคิด",
   "Have you had a system slow down or stop because a disk was full or the internet link was overloaded?",
   "เคยมีระบบช้าหรือหยุดเพราะดิสก์เต็มหรืออินเทอร์เน็ตเกินกำลังหรือไม่")

# ---------- DE.CM ----------
fr("DE.CM-01",
   "Attackers often stay inside a network for weeks before striking. Watching network activity is how you catch them early.",
   "ผู้โจมตีมักแฝงอยู่ในเครือข่ายหลายสัปดาห์ก่อนลงมือ การเฝ้าดูกิจกรรมบนเครือข่ายช่วยจับได้ตั้งแต่เนิ่น ๆ",
   "If an attacker were copying data out of your network at 2 a.m. tonight, who would notice, and when?",
   "หากคืนนี้ตีสองผู้โจมตีกำลังคัดลอกข้อมูลออกจากเครือข่าย ใครจะสังเกตเห็น และเมื่อใด")
fr("DE.CM-02",
   "Cameras, door alarms, and access logs detect physical intrusion, which can lead to IT compromise.",
   "กล้องวงจรปิด สัญญาณเตือนประตู และบันทึกการเข้าออก ช่วยตรวจจับการบุกรุกทางกายภาพซึ่งอาจนำไปสู่การบุกรุกระบบ IT",
   "If someone entered a restricted room at night, would anyone be alerted, or would you only see it on video later?",
   "หากมีคนเข้าห้องหวงห้ามตอนกลางคืน จะมีการแจ้งเตือนใครหรือไม่ หรือจะเห็นจากวิดีโอภายหลังเท่านั้น")
fr("DE.CM-03",
   "Unusual user behavior, such as logins at odd hours or large downloads, can signal a stolen account or an insider.",
   "พฤติกรรมผู้ใช้ที่ผิดปกติ เช่น เข้าสู่ระบบในเวลาแปลก ๆ หรือดาวน์โหลดจำนวนมาก อาจเป็นสัญญาณของบัญชีที่ถูกขโมยหรือบุคคลภายใน",
   "If an employee downloaded thousands of customer records the week before resigning, would anyone notice?",
   "หากพนักงานดาวน์โหลดข้อมูลลูกค้าหลายพันรายการในสัปดาห์ก่อนลาออก จะมีใครสังเกตเห็นหรือไม่")
fr("DE.CM-06",
   "Suppliers with access to your systems should be watched like your own staff, because their accounts are attractive targets.",
   "ผู้ให้บริการที่เข้าถึงระบบขององค์กรควรถูกเฝ้าระวังเหมือนพนักงานขององค์กรเอง เพราะบัญชีของเขาเป็นเป้าหมายที่น่าสนใจ",
   "If a vendor logged in remotely on a Sunday without being asked, would you know?",
   "หากผู้ขายเข้าสู่ระบบจากระยะไกลในวันอาทิตย์โดยไม่มีใครเรียก องค์กรจะรู้หรือไม่")
fr("DE.CM-09",
   "Antivirus and endpoint tools detect malware on computers and servers. They only help if they cover every device and someone reads the alerts.",
   "Antivirus และเครื่องมือป้องกันเครื่องลูกข่ายช่วยตรวจจับมัลแวร์บนคอมพิวเตอร์และเซิร์ฟเวอร์ แต่จะได้ผลก็ต่อเมื่อครอบคลุมทุกเครื่องและมีคนอ่านการแจ้งเตือน",
   "If antivirus flagged malware on a computer in accounting right now, who would receive that alert?",
   "หาก Antivirus แจ้งเตือนมัลแวร์บนคอมพิวเตอร์ฝ่ายบัญชีตอนนี้ ใครจะได้รับการแจ้งเตือนนั้น")

# ---------- DE.AE ----------
fr("DE.AE-02",
   "An alert is only a clue. Someone must investigate to decide whether it is harmless or the start of an attack.",
   "การแจ้งเตือนเป็นเพียงเบาะแส ต้องมีคนตรวจสอบเพื่อตัดสินว่าไม่มีอันตรายหรือเป็นจุดเริ่มต้นของการโจมตี",
   "Tell me about the last security alert your team investigated. What did they check, and how did they decide?",
   "เล่าถึงการแจ้งเตือนด้านความมั่นคงปลอดภัยครั้งล่าสุดที่ทีมตรวจสอบ ทีมตรวจอะไร และตัดสินอย่างไร")
fr("DE.AE-03",
   "One alert alone may look harmless. Combining logs from many systems shows the full story of an attack.",
   "การแจ้งเตือนเดียวอาจดูไม่มีอะไร การนำบันทึกจากหลายระบบมารวมกันช่วยให้เห็นเรื่องราวทั้งหมดของการโจมตี",
   "If a failed login on the VPN and a strange file on a server happened together, would anyone connect the two?",
   "หากมีการเข้าสู่ VPN ไม่สำเร็จและพบไฟล์แปลกบนเซิร์ฟเวอร์ในเวลาเดียวกัน จะมีใครเชื่อมโยงสองเรื่องนี้หรือไม่")
fr("DE.AE-04",
   "Knowing how big an event is decides how hard to respond: one infected laptop is different from a compromised server.",
   "การรู้ขนาดของเหตุการณ์เป็นตัวกำหนดระดับการรับมือ โน้ตบุ๊กติดมัลแวร์เครื่องเดียวต่างจากเซิร์ฟเวอร์ที่ถูกยึด",
   "If malware were found on one computer, how would the team check whether it had spread elsewhere?",
   "หากพบมัลแวร์บนคอมพิวเตอร์เครื่องหนึ่ง ทีมจะตรวจอย่างไรว่าแพร่ไปเครื่องอื่นแล้วหรือไม่")
fr("DE.AE-06",
   "Alerts must reach the right person quickly, including outside office hours.",
   "การแจ้งเตือนต้องไปถึงคนที่ใช่อย่างรวดเร็ว รวมถึงนอกเวลาทำการ",
   "If your monitoring provider detected an attack at midnight, whose phone would ring?",
   "หากผู้ให้บริการเฝ้าระวังตรวจพบการโจมตีตอนเที่ยงคืน โทรศัพท์ของใครจะดัง")
fr("DE.AE-07",
   "Knowing what attackers are doing elsewhere, and which systems matter most here, helps analysts judge alerts correctly.",
   "การรู้ว่าผู้โจมตีกำลังทำอะไรที่อื่น และระบบใดสำคัญที่สุดในองค์กร ช่วยให้ผู้วิเคราะห์ตัดสินการแจ้งเตือนได้ถูกต้อง",
   "When an alert comes in, does the analyst know whether the affected server is critical to the business?",
   "เมื่อมีการแจ้งเตือนเข้ามา ผู้วิเคราะห์รู้หรือไม่ว่าเซิร์ฟเวอร์ที่ได้รับผลกระทบสำคัญต่อธุรกิจเพียงใด")
fr("DE.AE-08",
   "Someone must decide when an event becomes an incident, because that starts the response plan, management escalation, and possibly legal reporting.",
   "ต้องมีคนตัดสินว่าเมื่อใดเหตุการณ์ทั่วไปกลายเป็นเหตุการณ์ด้านความมั่นคงปลอดภัย เพราะจะเริ่มแผนรับมือ การยกระดับถึงผู้บริหาร และอาจต้องรายงานตามกฎหมาย",
   "Who decides that 'we have an incident', and what makes them decide?",
   "ใครเป็นผู้ตัดสินว่า 'เรากำลังเผชิญเหตุการณ์' และอะไรทำให้เขาตัดสินเช่นนั้น")

# ---------- RS.MA ----------
fr("RS.MA-01",
   "In a serious incident you will need outside help: IT vendors, a forensic firm, lawyers, insurers. That help is fastest when agreed in advance.",
   "ในเหตุการณ์ร้ายแรง องค์กรจะต้องการความช่วยเหลือจากภายนอก เช่น ผู้ขาย IT บริษัทนิติวิทยาศาสตร์ดิจิทัล ทนายความ และบริษัทประกันภัย ความช่วยเหลือจะเร็วที่สุดเมื่อตกลงไว้ล่วงหน้า",
   "If you confirmed a ransomware attack this morning, who outside the organization would you call first, and do you already have a contract with them?",
   "หากเช้านี้ยืนยันได้ว่าโดนแรนซัมแวร์ ท่านจะโทรหาใครนอกองค์กรเป็นคนแรก และมีสัญญากับเขาไว้แล้วหรือไม่")
fr("RS.MA-02",
   "Not every report is a real incident. Quick checking separates false alarms from real attacks.",
   "ไม่ใช่ทุกรายงานที่เป็นเหตุการณ์จริง การตรวจสอบอย่างรวดเร็วช่วยแยกสัญญาณผิดพลาดออกจากการโจมตีจริง",
   "If a staff member reported a strange pop-up on their screen, what would happen next, step by step?",
   "หากพนักงานแจ้งว่ามีหน้าต่างแปลก ๆ ขึ้นบนหน้าจอ ขั้นตอนต่อไปจะเป็นอย่างไรทีละขั้น")
fr("RS.MA-03",
   "Incidents differ in seriousness. Clear categories ensure the worst ones get attention first.",
   "เหตุการณ์มีความรุนแรงต่างกัน การจัดประเภทที่ชัดเจนช่วยให้เหตุการณ์ร้ายแรงที่สุดได้รับความสนใจก่อน",
   "If one virus on a laptop and one suspected patient data leak were reported at the same time, which would the team handle first?",
   "หากมีรายงานไวรัสในโน้ตบุ๊กหนึ่งเครื่อง และสงสัยว่าข้อมูลผู้รับบริการรั่วไหลในเวลาเดียวกัน ทีมจะจัดการเรื่องใดก่อน")
fr("RS.MA-04",
   "Some decisions during an incident belong to management: shutting down systems, informing customers, or calling the police.",
   "การตัดสินใจบางอย่างระหว่างเหตุการณ์เป็นของผู้บริหาร เช่น การปิดระบบ การแจ้งลูกค้า หรือการแจ้งตำรวจ",
   "If shutting down the internet would stop an attack but halt operations, who has authority to make that call at night?",
   "หากการตัดอินเทอร์เน็ตจะหยุดการโจมตีได้แต่ทำให้การดำเนินงานหยุด ใครมีอำนาจตัดสินใจเรื่องนี้ตอนกลางคืน")
fr("RS.MA-05",
   "Restoring systems too early can bring the attacker back. Recovery should start only when clear conditions are met.",
   "การกู้คืนระบบเร็วเกินไปอาจทำให้ผู้โจมตีกลับมา การกู้คืนควรเริ่มเมื่อเป็นไปตามเงื่อนไขที่ชัดเจนเท่านั้น",
   "During an incident, how would you decide it is safe to start bringing systems back?",
   "ระหว่างเกิดเหตุ ท่านจะตัดสินอย่างไรว่าปลอดภัยพอที่จะเริ่มนำระบบกลับมาใช้")

# ---------- RS.AN ----------
fr("RS.AN-03",
   "Without finding the root cause, the same attack can happen again next month.",
   "หากไม่หาสาเหตุที่แท้จริง การโจมตีแบบเดิมอาจเกิดซ้ำได้ในเดือนหน้า",
   "After your last significant incident, could anyone explain exactly how the attacker got in?",
   "หลังเหตุการณ์สำคัญครั้งล่าสุด มีใครอธิบายได้ชัดเจนหรือไม่ว่าผู้โจมตีเข้ามาได้อย่างไร")
fr("RS.AN-06",
   "Records of what responders did protect the organization later, in front of regulators, insurers, or a court.",
   "บันทึกการดำเนินการของผู้รับมือเหตุการณ์ช่วยปกป้ององค์กรในภายหลัง ต่อหน้าหน่วยงานกำกับ บริษัทประกันภัย หรือศาล",
   "If your insurer asked for a timeline of every action taken during an incident, could you produce one?",
   "หากบริษัทประกันภัยขอลำดับเวลาของทุกการดำเนินการระหว่างเหตุการณ์ องค์กรจัดทำให้ได้หรือไม่")
fr("RS.AN-07",
   "Evidence such as logs and disk images disappears quickly. Collecting it properly matters if you want to claim insurance or take legal action.",
   "พยานหลักฐาน เช่น บันทึกและภาพดิสก์ หายไปได้เร็ว การเก็บอย่างถูกวิธีสำคัญหากต้องการเคลมประกันหรือดำเนินคดี",
   "If IT reinstalled an infected server immediately to restore service, what evidence would be lost?",
   "หาก IT ติดตั้งเซิร์ฟเวอร์ที่ติดมัลแวร์ใหม่ทันทีเพื่อให้บริการได้ หลักฐานใดจะหายไป")
fr("RS.AN-08",
   "How many records, people, or systems are affected decides legal reporting duties and the cost of the incident.",
   "จำนวนข้อมูล คน หรือระบบที่ได้รับผลกระทบ เป็นตัวกำหนดหน้าที่การรายงานตามกฎหมายและความเสียหายของเหตุการณ์",
   "If a database were leaked, how would you work out how many people's data was in it?",
   "หากฐานข้อมูลรั่วไหล ท่านจะหาจำนวนคนที่มีข้อมูลอยู่ในนั้นได้อย่างไร")

# ---------- RS.CO ----------
fr("RS.CO-02",
   "Thai law sets deadlines for reporting some incidents, for example 72 hours to the PDPC for personal data breaches. Missing them adds penalties to the damage.",
   "กฎหมายไทยกำหนดเวลาการรายงานเหตุการณ์บางประเภท เช่น แจ้ง สคส. ภายใน 72 ชั่วโมงเมื่อข้อมูลส่วนบุคคลรั่วไหล หากพลาดกำหนดจะมีโทษเพิ่มจากความเสียหาย",
   "If patient or customer data leaked on a Friday evening, who would decide whether to notify the PDPC, and could it be done by Monday evening?",
   "หากข้อมูลผู้รับบริการหรือลูกค้ารั่วไหลเย็นวันศุกร์ ใครเป็นผู้ตัดสินว่าจะแจ้ง สคส. หรือไม่ และจะแจ้งได้ทันภายในเย็นวันจันทร์หรือไม่")
fr("RS.CO-03",
   "Sharing the right information with partners, CERTs, and insurers helps the response. Sharing the wrong information can create legal risk.",
   "การแบ่งปันข้อมูลที่ถูกต้องกับคู่ค้า ศูนย์ CERT และบริษัทประกันภัยช่วยการรับมือ แต่การแบ่งปันข้อมูลผิดอาจสร้างความเสี่ยงทางกฎหมาย",
   "During an incident, who decides what to tell a business partner who asks 'are we affected?'",
   "ระหว่างเกิดเหตุ ใครเป็นผู้ตัดสินว่าจะบอกอะไรกับคู่ค้าที่ถามว่า 'เราได้รับผลกระทบหรือไม่'")

# ---------- RS.MI ----------
fr("RS.MI-01",
   "Containment means stopping the spread, for example isolating an infected computer or disabling a stolen account, within minutes.",
   "การควบคุมเหตุการณ์คือการหยุดการแพร่กระจาย เช่น แยกเครื่องที่ติดมัลแวร์หรือระงับบัญชีที่ถูกขโมย ภายในไม่กี่นาที",
   "If ransomware started spreading in one department, how quickly could IT cut that department off from the rest of the network?",
   "หากแรนซัมแวร์เริ่มแพร่ในแผนกหนึ่ง IT ตัดแผนกนั้นออกจากเครือข่ายส่วนอื่นได้เร็วเพียงใด")
fr("RS.MI-02",
   "Removing the attacker completely, including hidden accounts and back doors, prevents a second attack.",
   "การกำจัดผู้โจมตีให้หมด รวมถึงบัญชีที่ซ่อนไว้และประตูหลัง ช่วยป้องกันการโจมตีซ้ำ",
   "After an attack, how would you be sure the attacker did not leave a hidden way back in?",
   "หลังการโจมตี ท่านจะมั่นใจได้อย่างไรว่าผู้โจมตีไม่ได้ทิ้งช่องทางลับไว้กลับเข้ามา")

# ---------- RC.RP ----------
fr("RC.RP-01",
   "Recovery under pressure goes better when a plan says who leads and what happens in which order.",
   "การกู้คืนภายใต้ความกดดันจะดีกว่าเมื่อมีแผนบอกว่าใครเป็นผู้นำและทำอะไรตามลำดับใด",
   "During your last big outage, did people follow a written plan, or work it out as they went?",
   "ระหว่างระบบล่มครั้งใหญ่ล่าสุด ทุกคนทำตามแผนที่เป็นลายลักษณ์อักษร หรือแก้ไขกันไปตามสถานการณ์")
fr("RC.RP-02",
   "You cannot restore everything at once. The order should follow business priority, agreed before the crisis.",
   "การกู้คืนทุกอย่างพร้อมกันทำไม่ได้ ลำดับควรเป็นไปตามความสำคัญทางธุรกิจที่ตกลงไว้ก่อนเกิดวิกฤต",
   "If 30 systems were down, which would be restored first, and has the business agreed to that order?",
   "หากระบบ 30 ระบบล่มพร้อมกัน ระบบใดจะกู้คืนก่อน และฝ่ายธุรกิจเห็นชอบลำดับนั้นแล้วหรือไม่")
fr("RC.RP-03",
   "Restoring from an infected backup brings the attack back. Backups must be checked before use.",
   "การกู้คืนจากข้อมูลสำรองที่ติดมัลแวร์ทำให้การโจมตีกลับมา ต้องตรวจข้อมูลสำรองก่อนใช้",
   "If the attacker had been inside for three weeks, how would you know which backup is clean?",
   "หากผู้โจมตีแฝงอยู่ในระบบมา 3 สัปดาห์ ท่านจะรู้ได้อย่างไรว่าข้อมูลสำรองชุดใดสะอาด")
fr("RC.RP-04",
   "After a major incident, the business may run differently for a while, with manual work and extra controls.",
   "หลังเหตุการณ์ใหญ่ ธุรกิจอาจต้องทำงานต่างไปจากเดิมระยะหนึ่ง เช่น ทำงานด้วยมือและเพิ่มการควบคุม",
   "If your core system were unavailable for a week, how would critical work continue, on paper or another system?",
   "หากระบบหลักใช้งานไม่ได้หนึ่งสัปดาห์ งานสำคัญจะดำเนินต่ออย่างไร ใช้กระดาษหรือระบบอื่น")
fr("RC.RP-05",
   "A system that starts up is not necessarily working correctly. Owners should confirm data and functions are right before full use.",
   "ระบบที่เปิดขึ้นได้ไม่ได้แปลว่าทำงานถูกต้อง เจ้าของระบบควรยืนยันความถูกต้องของข้อมูลและการทำงานก่อนใช้งานเต็มรูปแบบ",
   "After IT restores a system, who checks that the data is complete and correct before staff use it again?",
   "หลัง IT กู้คืนระบบ ใครตรวจว่าข้อมูลครบถ้วนและถูกต้องก่อนให้พนักงานกลับมาใช้")
fr("RC.RP-06",
   "Formally closing an incident ensures reports are finished and lessons are captured, instead of everyone moving on.",
   "การปิดเหตุการณ์อย่างเป็นทางการช่วยให้รายงานเสร็จสมบูรณ์และได้บทเรียน แทนที่ทุกคนจะผ่านเลยไป",
   "For your last incident, was there a final report and a meeting on what to do differently?",
   "สำหรับเหตุการณ์ครั้งล่าสุด มีรายงานฉบับสมบูรณ์และการประชุมว่าจะทำอะไรต่างออกไปหรือไม่")

# ---------- RC.CO ----------
fr("RC.CO-03",
   "During a long outage, staff, management, and customers want regular updates. Silence creates rumors.",
   "ระหว่างระบบล่มเป็นเวลานาน พนักงาน ผู้บริหาร และลูกค้าต้องการข้อมูลความคืบหน้าสม่ำเสมอ ความเงียบทำให้เกิดข่าวลือ",
   "If email and LINE were both unavailable during an outage, how would you send updates to all department heads?",
   "หากอีเมลและ LINE ใช้งานไม่ได้ทั้งคู่ระหว่างระบบล่ม ท่านจะส่งข้อมูลความคืบหน้าถึงหัวหน้าทุกฝ่ายอย่างไร")
fr("RC.CO-04",
   "What the organization says in public during an incident affects trust, legal exposure, and the regulator's view.",
   "สิ่งที่องค์กรสื่อสารต่อสาธารณะระหว่างเหตุการณ์มีผลต่อความเชื่อมั่น ความเสี่ยงทางกฎหมาย และมุมมองของหน่วยงานกำกับ",
   "If a news reporter called during an incident, who would speak, and is a prepared statement ready?",
   "หากนักข่าวโทรมาระหว่างเกิดเหตุ ใครเป็นผู้ให้ข้อมูล และมีแถลงการณ์ที่เตรียมไว้แล้วหรือไม่")

if __name__ == "__main__":
    print(len(F))
