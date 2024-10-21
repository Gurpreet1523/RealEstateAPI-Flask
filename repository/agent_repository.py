from models.models import Agent, db


class AgentRepository:

    @staticmethod
    def get_all_agents():
        return Agent.query.all()

    @staticmethod
    def create_agent(agent):
        db.session.add(agent)
        db.session.commit()

    @staticmethod
    def get_agent(agent_id):
        return Agent.query.filter_by(agent_id=agent_id).first()

    @staticmethod
    def update_agent(agent_id, data):
        agent = Agent.query.filter_by(agent_id=agent_id).first()
        if agent:
            for key, value in data.items():
                setattr(agent, key, value)
            db.session.commit()
        return agent

    @staticmethod
    def delete_agent(agent_id):
        agent = Agent.query.filter_by(agent_id=agent_id).first()
        if agent:
            db.session.delete(agent)
            db.session.commit()
            return True
        return False
