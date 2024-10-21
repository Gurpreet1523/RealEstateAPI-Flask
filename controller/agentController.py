from flask import Blueprint, request, jsonify
from services.agent_service import AgentService
from flask_jwt_extended import jwt_required, get_jwt_identity

agent_bp = Blueprint('agent_bp', __name__)


@agent_bp.route('/agents', methods=['POST'])
@jwt_required()
def create_new_agent():
    current_user = get_jwt_identity()
    data = request.get_json()
    agent = AgentService.create_agent(current_user, data)
    return jsonify({"agent_id": agent.agent_id, "agency_name": agent.agency_name}), 201


@agent_bp.route('/agents', methods=['GET'])
def get_properties():
    agents = AgentService.get_all_agents()
    return jsonify([agent.to_dict() for agent in agents]), 200


@agent_bp.route('/agents/<int:agent_id>', methods=['GET'])
def get_agent_details(agent_id):
    agent = AgentService.get_agent_by_id(agent_id)
    if not agent:
        return jsonify({"message": "Agent not found"}), 404
    return jsonify({"agent_id": agent.agent_id, "agency_name": agent.agency_name, "phone_number": agent.phone_number,
                    "email": agent.email}), 200


@agent_bp.route('/agents/<int:agent_id>', methods=['PUT'])
@jwt_required()
def update_agent_details(agent_id):
    data = request.get_json()
    agent = AgentService.update_agent(agent_id, data)
    if not agent:
        return jsonify({"message": "Agent not found"}), 404
    return jsonify({"message": "Agent updated successfully"}), 200


@agent_bp.route('/agents/<int:agent_id>', methods=['DELETE'])
@jwt_required()
def delete_agent_details(agent_id):
    agent = AgentService.delete_agent(agent_id)
    if not agent:
        return jsonify({"message": "Agent not found"}), 404
    return jsonify({"message": "Agent deleted successfully"}), 200
