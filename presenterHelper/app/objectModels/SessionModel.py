__author__ = 'farzin'


class SessionModel:

	def __init__(self, session, p_name, participant_size):
		self.name = session.name
		self.presentation_name = p_name
		self.code =session.code
		self.is_active = session.is_active
		self.end_date = session.end_date
		self.current_page = session.current_page
		self.participant_size = participant_size

