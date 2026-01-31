import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artifa_fest.settings')
django.setup()

from core.models import ChatbotTraining

# Update all short records with proper detailed answers
updates = {
    # Venue questions
    "Where are events held?": "<div class='venue-info'><h4>Event Venues at National Engineering College</h4><p><strong>ARTIFA FEST events</strong> are strategically distributed across the campus to ensure optimal participation and technical requirements:</p><div class='venue-details'><p><strong>🏢 Computer Laboratories:</strong> Dedicated for coding competitions, hackathons, and technical events requiring computing resources</p><p><strong>🏫 Smart Classrooms:</strong> Equipped with projectors and audio systems for presentations, workshops, and seminars</p><p><strong>🎭 Auditorium:</strong> Main venue for opening ceremonies, prize distributions, and large gatherings</p><p><strong>🌳 Open Areas:</strong> Designated spaces for outdoor activities, team formations, and networking breaks</p><p><strong>🔬 Department Labs:</strong> Specialized laboratories for AI&DS, electronics, and mechanical events</p></div><p>All venues are easily accessible within the campus and equipped with necessary facilities including WiFi, power outlets, and technical support.</p></div>",

    "Event locations": "<div class='venue-info'><h4>ARTIFA FEST Venue Locations</h4><p>Our events are hosted across multiple campus locations to provide the best environment for each activity type:</p><ul><li><strong>Technical Events:</strong> Computer labs and department buildings</li><li><strong>Creative Events:</strong> Design studios and presentation halls</li><li><strong>Gaming Events:</strong> Recreation areas and common rooms</li><li><strong>Sports Events:</strong> Open grounds and indoor sports facilities</li><li><strong>Main Events:</strong> Central auditorium and main hall</li></ul><p>Clear signage and volunteer guides will help you navigate to the correct venues. All locations are within walking distance on our compact campus.</p></div>",

    "Where do events take place?": "<div class='venue-info'><h4>Event Venue Information</h4><p><strong>National Engineering College</strong> provides excellent facilities for hosting ARTIFA FEST across multiple campus locations:</p><div class='venue-grid'><div class='venue-item'><h5>🎯 Technical Hub</h5><p>Computer labs, programming centers, and tech workshops</p></div><div class='venue-item'><h5>🎨 Creative Spaces</h5><p>Design studios, art rooms, and presentation areas</p></div><div class='venue-item'><h5>⚡ Activity Zones</h5><p>Open grounds, recreation areas, and common spaces</p></div></div><p>Each venue is selected based on the specific requirements of the event to ensure participants have the best possible experience.</p></div>",

    "Venue information": "<div class='venue-info'><h4>Comprehensive Venue Guide</h4><p>ARTIFA FEST utilizes the entire National Engineering College campus infrastructure:</p><ul><li><strong>🏛️ Academic Buildings:</strong> Classrooms and lecture halls for theory-based events</li><li><strong>💻 Technology Centers:</strong> Computer labs with latest equipment and software</li><li><strong>🎪 Recreation Facilities:</strong> Indoor and outdoor spaces for games and activities</li><li><strong>📚 Library & Study Areas:</strong> Quiet zones for preparation and research</li><li><strong>🍽️ Support Areas:</strong> Cafeteria and rest areas for breaks</li></ul><p>Our campus layout ensures easy movement between venues, and all areas are equipped with modern amenities and accessibility features.</p></div>",

    # Schedule questions
    "Event schedule": "<div class='schedule-info'><h4>ARTIFA FEST 2026 - Complete Schedule</h4><p>Our meticulously planned schedule ensures maximum participation and minimal conflicts:</p><div class='schedule-timeline'><h5>📅 Morning Session (10:30 AM - 12:30 PM)</h5><ul><li>Technical competitions and coding challenges</li><li>Creative workshops and design events</li><li>Data analytics and research presentations</li><li>AI and machine learning demonstrations</li></ul><h5>🏖️ Afternoon Session (2:30 PM - 4:30 PM)</h5><ul><li>Strategic games and board challenges</li><li>Team-based activities and competitions</li><li>Interactive sessions and fun events</li><li>Closing ceremonies and prize distributions</li></ul></div><p>All timings are designed to accommodate travel, preparation, and breaks between events.</p></div>",

    "When are events happening?": "<div class='schedule-info'><h4>Event Timing Overview</h4><p><strong>ARTIFA FEST</strong> features a well-structured timeline across the event day:</p><div class='timing-details'><p><strong>⏰ Morning Events (10:30 AM - 12:30 PM):</strong> Technical and creative competitions requiring focused attention</p><p><strong>🍽️ Lunch Break (12:30 PM - 2:30 PM):</strong> Time for networking and refreshments</p><p><strong>🎮 Afternoon Events (2:30 PM - 4:30 PM):</strong> Interactive games and strategic challenges</p><p><strong>🏆 Evening Activities (4:30 PM onwards):</strong> Prize distributions and closing ceremonies</p></div><p>This schedule allows participants to engage in multiple events while ensuring adequate rest and preparation time.</p></div>",

    "Event timings": "<div class='schedule-info'><h4>Detailed Event Timings</h4><p>Precise scheduling ensures smooth execution of all ARTIFA FEST activities:</p><table class='timing-table'><tr><th>Time Slot</th><th>Activities</th><th>Duration</th></tr><tr><td>10:30 AM - 12:30 PM</td><td>Morning Technical Sessions</td><td>2 hours</td></tr><tr><td>12:30 PM - 2:30 PM</td><td>Lunch & Networking</td><td>2 hours</td></tr><tr><td>2:30 PM - 4:30 PM</td><td>Afternoon Activities</td><td>2 hours</td></tr><tr><td>4:30 PM - 5:30 PM</td><td>Results & Awards</td><td>1 hour</td></tr></table><p>Each time slot is carefully allocated to provide sufficient time for meaningful participation and evaluation.</p></div>",

    "Schedule overview": "<div class='schedule-info'><h4>ARTIFA FEST Schedule Overview</h4><p><strong>Day-long celebration</strong> of technology, creativity, and innovation featuring:</p><div class='schedule-highlights'><h5>🌅 Morning Phase</h5><p>Technical excellence and creative expression through coding, design, and analytical challenges</p><h5>🌞 Afternoon Phase</h5><p>Strategic thinking and teamwork through games, auctions, and interactive competitions</p><h5>🌆 Evening Phase</h5><p>Recognition and celebration of achievements with awards and networking opportunities</p></div><p>The schedule is designed to maintain energy levels and provide diverse experiences throughout the day.</p></div>",

    # Contact/Support questions
    "Who to contact for help?": "<div class='contact-info'><h4>ARTIFA FEST Support Contacts</h4><p>Multiple channels available for assistance throughout the event:</p><div class='contact-channels'><h5>📧 Email Support</h5><ul><li><strong>General Queries:</strong> artifa.fest@nec.edu.in</li><li><strong>Technical Issues:</strong> tech.support@nec.edu.in</li><li><strong>Registration Help:</strong> registration@nec.edu.in</li><li><strong>Event Coordinators:</strong> coordinators@nec.edu.in</li></ul><h5>📱 On-site Support</h5><ul><li><strong>Student Volunteers:</strong> Available at all venues</li><li><strong>Faculty Coordinators:</strong> Department representatives</li><li><strong>Help Desks:</strong> Main areas and registration points</li><li><strong>Emergency:</strong> Security and medical staff</li></ul></div><p>Don't hesitate to reach out - our team is here to ensure you have an excellent experience!</p></div>",

    "How to get help?": "<div class='contact-info'><h4>Getting Help at ARTIFA FEST</h4><p><strong>Multiple support options</strong> available throughout the event:</p><div class='help-options'><h5>🚀 Immediate Assistance</h5><ul><li>Approach any volunteer or coordinator at the venue</li><li>Use the help desks located in main areas</li><li>Contact event-specific support teams</li><li>Reach out to faculty supervisors</li></ul><h5>📞 Communication Channels</h5><ul><li>Email the respective coordinators</li><li>Use the event mobile numbers</li><li>Post queries on official social media</li><li>Visit the registration office</li></ul><h5>🛠️ Technical Support</h5><ul><li>IT help desks for technical issues</li><li>Equipment support and troubleshooting</li><li>Internet and connectivity assistance</li><li>Software and tool guidance</li></ul></div><p>Our support team is committed to resolving issues quickly and ensuring smooth participation.</p></div>",

    "Support contact": "<div class='contact-info'><h4>Support Contact Information</h4><p><strong>ARTIFA FEST Support Network:</strong></p><div class='support-grid'><div class='support-item'><h5>👥 General Support</h5><p>Event coordinators and volunteers</p><p>📞 Available at venue</p></div><div class='support-item'><h5>💻 Technical Support</h5><p>IT team and technical volunteers</p><p>🖥️ Computer labs and help desks</p></div><div class='support-item'><h5>📋 Registration Support</h5><p>Registration team and coordinators</p><p>📝 Main registration area</p></div><div class='support-item'><h5>🚨 Emergency Support</h5><p>Security and medical staff</p><p>📱 Emergency numbers displayed</p></div></div><p>All support personnel are easily identifiable and ready to assist with any queries or issues.</p></div>",

    "Help desk": "<div class='contact-info'><h4>Help Desk Services</h4><p><strong>Strategic help desks</strong> positioned throughout the campus for immediate assistance:</p><div class='help-desk-info'><h5>📍 Location & Services</h5><ul><li><strong>Main Entrance:</strong> Registration and general queries</li><li><strong>Computer Labs:</strong> Technical support and equipment help</li><li><strong>Auditorium Area:</strong> Event coordination and scheduling</li><li><strong>Recreation Areas:</strong> Activity guidance and team formation</li></ul><h5>🛠️ Available Services</h5><ul><li>Registration assistance and corrections</li><li>Technical troubleshooting and guidance</li><li>Event information and clarifications</li><li>Emergency support and first aid</li><li>Directions and venue guidance</li></ul></div><p>Help desks are staffed by trained volunteers and coordinators throughout the event duration.</p></div>"
}

# Update short records
updated_count = 0
short_records = ChatbotTraining.objects.filter().extra(where=["LENGTH(answer) < 500"])

for record in short_records:
    question_lower = record.question.lower().strip()
    for key, new_answer in updates.items():
        if key.lower() in question_lower:
            record.answer = new_answer
            record.save()
            updated_count += 1
            break

print(f"Updated {updated_count} short records with detailed answers")

# Final verification
final_short = ChatbotTraining.objects.filter().extra(where=["LENGTH(answer) < 500"])
print(f"Remaining short records: {final_short.count()}")

total_records = ChatbotTraining.objects.count()
print(f"Total records: {total_records}")