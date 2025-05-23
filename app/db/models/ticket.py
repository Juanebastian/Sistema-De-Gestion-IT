from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base
from app.db.models.area import Area

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    asunto = Column(String(150), nullable=False)
    descripcion = Column(Text)
    estado_id = Column(Integer, ForeignKey("estados_ticket.id"), nullable=False)
    prioridad_id = Column(Integer, ForeignKey("prioridades_ticket.id"))
    id_creador = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    id_tecnico = Column(Integer, ForeignKey("usuarios.id"))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)
    fecha_cierre = Column(DateTime, nullable=True)
    area_id = Column(Integer, ForeignKey("areas.id"))

    # Relaciones
    estado = relationship("Estado", backref="tickets")
    prioridad = relationship("Prioridad", backref="tickets")
    creador = relationship("Usuario", foreign_keys=[id_creador])
    tecnico = relationship("Usuario", foreign_keys=[id_tecnico])
    area = relationship("Area", backref="tickets")  # Nueva relación agregada



class Estado(Base):
    __tablename__ = "estados_ticket"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)


class Prioridad(Base):
    __tablename__ = "prioridades_ticket"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)