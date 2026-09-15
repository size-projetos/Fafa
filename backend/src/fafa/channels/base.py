"""Contrato comum dos canais.

Um canal recebe texto de um usuario, entrega ao Agente com um `sessao_id`
estavel e devolve a resposta pelo mesmo meio. Tambem pode enviar avisos
espontaneos (notificar), que e como o Fafa chama o Daniel quando termina uma
tarefa longa e ele ja saiu da frente do computador.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from fafa.core.agent import Agente, Resposta


class Canal(ABC):
    nome: str = "canal"

    def __init__(self, agente: Agente) -> None:
        self.agente = agente

    def sessao_id(self, usuario: str) -> str:
        return f"{self.nome}:{usuario}"

    def processar(self, usuario: str, texto: str, ao_progresso=None) -> Resposta:
        """Caminho padrao: entrega ao agente e devolve a resposta."""
        return self.agente.responder(
            texto,
            sessao_id=self.sessao_id(usuario),
            canal=self.nome,
            usuario=usuario,
            ao_progresso=ao_progresso,
        )

    @abstractmethod
    def enviar(self, usuario: str, texto: str) -> None:
        """Envia um texto ao usuario por este canal (resposta ou aviso)."""

    def notificar(self, usuario: str, texto: str) -> None:
        """Aviso espontaneo. Por padrao e um `enviar` comum."""
        self.enviar(usuario, texto)
