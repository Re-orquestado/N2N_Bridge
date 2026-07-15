from pydantic import BaseModel, Field
from typing import Literal, Optional


# ── Input models ──────────────────────────────────────────────────────────────

EnemyProximity = Literal["none", "distant", "near", "close"]
Environment = Literal[
    "dark_cave", "dungeon", "crypt",
    "forest", "meadow", "village",
    "underwater", "ocean",
    "city", "ruins",
    "boss_arena", "sanctuary",
    "generic",
]
TransitionType = Literal["smooth", "abrupt", "crossfade", "cut", "stinger"]
TargetEmotion = Literal[
    "calm", "curious", "tense", "urgent_survival",
    "triumphant", "mournful", "mysterious", "heroic",
    "dread", "relief", "epic",
]


class GameState(BaseModel):
    player_health: float = Field(..., ge=0, le=100, description="Player HP 0–100")
    enemy_proximity: EnemyProximity = Field(default="none")
    environment: Environment = Field(default="generic")
    narrative_tension_level: float = Field(
        ..., ge=0, le=10, description="Story tension 0–10"
    )
    is_in_combat: bool = False


class MusicalRequest(BaseModel):
    transition_type: TransitionType = "smooth"
    target_emotion: TargetEmotion = "calm"


class AdaptiveMusicRequest(BaseModel):
    game_state: GameState
    musical_request: MusicalRequest


# ── Output models ─────────────────────────────────────────────────────────────

Scale = Literal["major", "minor", "dorian", "phrygian", "lydian", "diminished", "harmonic_minor"]
Layer = Literal[
    "percussion", "bass", "strings", "brass", "woodwinds",
    "choir", "ambient_pad", "piano", "guitar", "synth",
    "heartbeat_pulse", "nature_sounds",
]
Effect = Literal[
    "reverb_small", "reverb_large", "cave_echo",
    "chorus", "low_pass_filter", "high_pass_filter",
    "distortion", "compression", "tremolo",
    "filter_sweep", "stereo_widener", "sub_bass_boost",
    "underwater_warp", "heartbeat_lfo",
]


class TransitionParams(BaseModel):
    type: TransitionType
    duration_ms: int = Field(..., description="Cross-fade or fade duration in ms")
    curve: Literal["instant", "linear", "ease_in", "ease_out", "ease_in_out"]


class MixParameters(BaseModel):
    reverb_amount: float = Field(..., ge=0.0, le=1.0)
    bass_boost: float = Field(..., ge=0.0, le=1.0)
    compression: float = Field(..., ge=0.0, le=1.0)
    stereo_width: float = Field(..., ge=0.0, le=1.0)
    high_pass_cutoff_hz: Optional[int] = None
    low_pass_cutoff_hz: Optional[int] = None


class ReasoningFactors(BaseModel):
    health_factor: str
    proximity_factor: str
    environment_factor: str
    tension_factor: str
    emotion_factor: str


class MusicProfile(BaseModel):
    tempo_bpm: int
    musical_key: str
    scale: Scale
    intensity: float = Field(..., ge=0.0, le=1.0)
    layers: list[Layer]
    effects: list[Effect]
    transition: TransitionParams
    mood_tags: list[str]
    mix_parameters: MixParameters


class AdaptiveMusicResponse(BaseModel):
    music_profile: MusicProfile
    reasoning: ReasoningFactors


# ── N2N Bridge models (estructura plana para el endpoint /generate) ────────────

class N2NMusicalRequest(BaseModel):
    emotions: list[str] = Field(
        ..., description='Emociones objetivo, ej. ["tenso", "misterioso"]'
    )


class TelemetryData(BaseModel):
    player_health: float = Field(..., ge=0, le=100, description="HP del jugador 0–100")
    enemy_proximity: float = Field(..., ge=0, le=100, description="Proximidad enemigo 0–100")
    environment: str = Field(..., description='Ambiente, ej. "dark_cave"')
    narrative_tension_level: int = Field(..., ge=1, le=10, description="Tensión narrativa 1–10")
    is_in_combat: bool = Field(default=False)
    musical_request: N2NMusicalRequest
