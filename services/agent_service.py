from repository.agent_repository import AgentRepository
from models.models import Agent


class AgentService:

    @staticmethod
    def create_agent(user_id, data):
        agent = Agent(
            user_id=user_id,
            agency_name=data.get('agency_name'),
            phone_number=data.get('phone_number'),
            email=data.get('email')
        )
        AgentRepository.create_agent(agent)
        return agent

    @staticmethod
    def get_all_agents():
        return AgentRepository.get_all_agents()

    @staticmethod
    def get_agent_by_id(agent_id):
        return AgentRepository.get_agent(agent_id)

    @staticmethod
    def update_agent(agent_id, data):
        agent = AgentRepository.get_agent(agent_id)
        if agent:
            agent.agency_name = data.get('agency_name', agent.agency_name)
            agent.phone_number = data.get('phone_number', agent.phone_number)
            agent.email = data.get('email', agent.email)
            AgentRepository.update_agent(agent_id, data)
        return agent

    @staticmethod
    def delete_agent(agent_id):
        agent = AgentRepository.get_agent(agent_id)
        if not agent:
            return False
        return AgentRepository.delete_agent(agent_id)
