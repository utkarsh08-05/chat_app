from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Count, Max
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Message
from .utils import is_user_online


# =========================
# MAIN CHAT VIEW
# =========================
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Count, Max
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Message
from .utils import is_user_online


@login_required
def chat_home(request, user_id=None):
    # =========================
    # USERS LIST (LEFT SIDEBAR)
    # =========================
    users = (
        User.objects
        .exclude(id=request.user.id)
        .annotate(
            last_sent_time=Max(
                "sent_message__timestamp",
                filter=Q(sent_message__receiver=request.user)
            ),
            last_received_time=Max(
                "recieved_message__timestamp",
                filter=Q(recieved_message__sender=request.user)
            )
        )
    )

    # timezone-aware minimum datetime
    MIN_DT = timezone.make_aware(datetime.min)

    # Compute final last message time
    for u in users:
        u.last_message_time = max(
            u.last_sent_time or MIN_DT,
            u.last_received_time or MIN_DT
        )

    # Sort by latest conversation
    users = sorted(
        users,
        key=lambda u: u.last_message_time,
        reverse=True
    )

    # =========================
    # ATTACH LAST MESSAGE OBJECT
    # =========================
    for u in users:
        u.last_message = (
            Message.objects
            .filter(
                Q(sender=u, receiver=request.user) |
                Q(sender=request.user, receiver=u)
            )
            .order_by("-timestamp")
            .first()
        )

    # =========================
    # UNREAD MESSAGE COUNT
    # =========================
    unread_counts = (
        Message.objects
        .filter(receiver=request.user, is_seen=False)
        .values("sender")
        .annotate(count=Count("id"))
    )

    unread_map = {row["sender"]: row["count"] for row in unread_counts}

    for u in users:
        u.unread_count = unread_map.get(u.id, 0)

    # =========================
    # ACTIVE CHAT
    # =========================
    other_user = None

    if user_id:
        other_user = get_object_or_404(User, id=user_id)

        # Mark messages as seen when chat is open
        Message.objects.filter(
            sender=other_user,
            receiver=request.user,
            is_seen=False
        ).update(is_seen=True)

        # Send message
        if request.method == "POST":
            content = request.POST.get("content", "").strip()
            if content:
                Message.objects.create(
                    sender=request.user,
                    receiver=other_user,
                    content=content
                )
            return JsonResponse({"ok": True})

    # =========================
    # RENDER
    # =========================
    return render(request, "chat/chat_layout.html", {
        "users": users,
        "other_user": other_user,
    })

# =========================
# FETCH MESSAGES (AJAX)
# =========================
@login_required
def fetch_messages(request, user_id):
    after = request.GET.get("after")
    before = request.GET.get("before")

    qs = Message.objects.filter(
        Q(sender=request.user, receiver_id=user_id) |
        Q(sender_id=user_id, receiver=request.user)
    )

    if after:
        qs = qs.filter(id__gt=after)

    if before:
        qs = qs.filter(id__lt=before)

    messages = qs.order_by("id")[:30]

    # Mark received messages as seen (polling-safe)
    Message.objects.filter(
        sender_id=user_id,
        receiver=request.user,
        is_seen=False
    ).update(is_seen=True)

    data = [{
        "id": m.id,
        "sender": m.sender.username,
        "content": m.content,
        "timestamp": m.timestamp.strftime("%H:%M"),
        "seen": m.is_seen,
    } for m in messages]

    return JsonResponse({"messages": data})


# =========================
# USER ONLINE STATUS
# =========================
@login_required
def user_status(request, user_id):
    user = get_object_or_404(User, id=user_id)

    online = (
        user.profile.is_chat_active and
        is_user_online(user.profile)
    )

    return JsonResponse({"online": online})


# =========================
# CHAT PRESENCE
# =========================
@login_required
def chat_active(request):
    request.user.profile.is_chat_active = True
    request.user.profile.save(update_fields=["is_chat_active"])
    return JsonResponse({"ok": True})


@login_required
def chat_inactive(request):
    request.user.profile.is_chat_active = False
    request.user.profile.save(update_fields=["is_chat_active"])
    return JsonResponse({"ok": True})
