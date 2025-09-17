from odoo import http
from odoo.http import request
import json

class AIAssistantController(http.Controller):
    
    @http.route('/ai_assistant/generate', type='json', auth='user', methods=['POST'])
    def generate_text(self, **post):
        """Handle text generation requests from the web interface"""
        prompt = post.get('prompt')
        assistant_id = post.get('assistant_id')
        
        if not prompt:
            return {'error': 'No prompt provided'}
            
        assistant = request.env['ai.assistant'].browse(int(assistant_id)) if assistant_id else None
        if not assistant:
            assistant = request.env['ai.assistant'].search([], limit=1)
            if not assistant:
                return {'error': 'No AI assistant configured'}
        
        try:
            response = assistant.generate_text(prompt)
            return {'result': response}
        except Exception as e:
            return {'error': str(e)}
