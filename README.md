# Proyecto: Mensajeria

Este proyecto es una base para la creación de servicios de mensajería que puedan utilizar diferentes APIs de distintos proveedores. El objetivo es contar con un esqueleto reutilizable para implementar y extender servicios de mensajería como SMS y WhatsApp.

## Objetivos
- Crear un microservicio API capaz de enviar mensajes vía SMS y WhatsApp.
- Permitir la integración con múltiples proveedores de mensajería.
- Proveer una base escalable y mantenible para futuros servicios.

## Tecnologías
- .NET Core 8

## Proveedores a implementar
- **Twilio**
  - Investigar la API de Twilio, conocer sus capacidades y condiciones de uso.
  - Verificar si existe un plan gratuito para desarrollo y pruebas.
  - Implementar la integración para envío de mensajes SMS y WhatsApp.

## Arquitectura
- Microservicio API REST para envío de mensajes.
- Estructura modular para facilitar la integración de nuevos proveedores.

## Aplicación Cliente (Mock)
- Aplicación que consume la API de mensajería.
- Utiliza datos mock (simulados) para pruebas.
- Lista de números de teléfono con orden de prioridad.
- El sistema debe saber si el mensaje fue recibido por el usuario.
- Si no hay confirmación de recepción, el mensaje debe ser reenviado al siguiente número en la lista.

## Consideraciones
- El proyecto está pensado para ser la base de futuros servicios de mensajería.
- El código debe ser limpio, documentado y fácilmente extensible.
- Se recomienda investigar y documentar las capacidades y limitaciones de cada proveedor integrado.

---

