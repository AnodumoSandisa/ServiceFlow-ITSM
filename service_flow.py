import datetime

class ServiceFlow:
    """
    A Tech Consulting tool designed to translate technical issues 
    into business-aligned ITIL categories.
    """
    
    def __init__(self, user_name):
        self.user_name = user_name
        self.log_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def analyze_request(self, description):
        # Professional ITIL Keyword Mapping
        incident_triggers = ["broken", "not working", "down", "error", "failed"]
        security_triggers = ["hacked", "suspicious", "password reset", "phishing", "leak"]
        change_triggers = ["install", "update", "new user", "upgrade", "access request"]

        desc_lower = description.lower()

        
        if any(word in desc_lower for word in security_triggers):
            category = "🚨 SECURITY INCIDENT"
            priority = "CRITICAL"
            advice = "Immediate referral to Incident Response (Digital Forensics)."
        elif any(word in desc_lower for word in incident_triggers):
            category = "⚠️ INCIDENT"
            priority = "HIGH"
            advice = "Restore service as per SLA guidelines."
        elif any(word in desc_lower for word in change_triggers):
            category = "⚙️ CHANGE REQUEST"
            priority = "MEDIUM"
            advice = "Evaluate business impact and schedule for approval."
        else:
            category = "📖 SERVICE REQUEST"
            priority = "LOW"
            advice = "Provide standard administrative support."

        return self.generate_report(description, category, priority, advice)

    def generate_report(self, desc, cat, prio, adv):
        return f"""
---------------------------------------------------------
[ITIL ANALYSIS REPORT - {self.log_date}]
---------------------------------------------------------
Consultant Analyst: {self.user_name}
User Issue: "{desc}"

Resulting ITIL Category: {cat}
Priority Level: {prio}
Consulting Advice: {adv}
---------------------------------------------------------
        """


if __name__ == "__main__":
   
    consultant_tool = ServiceFlow("Anodumo - Tech Consulting Analyst")
    
    print(consultant_tool.analyze_request("I clicked a suspicious link in my email."))
    
   
    print(consultant_tool.analyze_request("We need to install new AI software for the public sector project."))