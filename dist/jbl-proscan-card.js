const JBL_PROSCAN_CARD_VERSION = "1.0.0";

const JBL_STRINGS = {
  fr: {
    card_name: "JBL ProScan",
    card_description: "Qualité de l’eau et historique JBL ProScan.",
    title_default: "Bassin — JBL ProScan",
    entity_required: "Sélectionnez le capteur Historique JBL ProScan.",
    entity_missing: "Entité introuvable",
    no_data: "Aucune analyse disponible",
    last_analysis: "Dernière analyse",
    today: "aujourd’hui",
    yesterday: "hier",
    days_ago: "il y a {days} jours",
    unknown_date: "date inconnue",
    good: "Bon",
    warning: "À surveiller",
    bad: "Mauvais",
    neutral: "Information",
    analyses: "analyses",
    analysis: "analyse",
    history: "Historique",
    latest_values: "Dernières mesures",
    measurements_shown: "{count} mesures affichées",
    preserved: "Les signes > et < sont conservés.",
    local_rating: "Évaluation locale configurable.",
    no_chart: "Pas assez de données pour tracer le graphique.",
    chlorine: "Chlore",
    editor_entity: "Entité Historique",
    editor_title: "Titre",
    editor_measurements: "Nombre de mesures",
    editor_show_co2: "Afficher le CO₂",
    editor_warning: "Avertissement après (jours)",
    editor_critical: "Critique après (jours)",
    editor_compact: "Mode compact",
    editor_help_entity: "Choisissez le capteur JBL ProScan dont l’attribut measurements contient l’historique.",
    age_warning: "Analyse ancienne",
    source: "Source"
  },
  en: {
    card_name: "JBL ProScan", card_description: "Water quality and JBL ProScan history.", title_default: "Pond — JBL ProScan",
    entity_required: "Select the JBL ProScan History sensor.", entity_missing: "Entity not found", no_data: "No analysis available", last_analysis: "Latest analysis",
    today: "today", yesterday: "yesterday", days_ago: "{days} days ago", unknown_date: "unknown date", good: "Good", warning: "Watch", bad: "Poor", neutral: "Information",
    analyses: "analyses", analysis: "analysis", history: "History", latest_values: "Latest readings", measurements_shown: "{count} measurements shown", preserved: "> and < signs are preserved.", local_rating: "Configurable local rating.", no_chart: "Not enough data to draw the chart.", chlorine: "Chlorine",
    editor_entity: "History entity", editor_title: "Title", editor_measurements: "Number of measurements", editor_show_co2: "Show CO₂", editor_warning: "Warning after (days)", editor_critical: "Critical after (days)", editor_compact: "Compact mode", editor_help_entity: "Choose the JBL ProScan sensor whose measurements attribute contains the history.", age_warning: "Old analysis", source: "Source"
  },
  de: {
    card_name: "JBL ProScan", card_description: "Wasserqualität und JBL-ProScan-Verlauf.", title_default: "Teich — JBL ProScan", entity_required: "Wähle den JBL-ProScan-Verlaufssensor.", entity_missing: "Entität nicht gefunden", no_data: "Keine Analyse verfügbar", last_analysis: "Letzte Analyse", today: "heute", yesterday: "gestern", days_ago: "vor {days} Tagen", unknown_date: "Datum unbekannt", good: "Gut", warning: "Beobachten", bad: "Schlecht", neutral: "Information", analyses: "Analysen", analysis: "Analyse", history: "Verlauf", latest_values: "Letzte Messwerte", measurements_shown: "{count} Messungen angezeigt", preserved: "Die Zeichen > und < bleiben erhalten.", local_rating: "Konfigurierbare lokale Bewertung.", no_chart: "Nicht genügend Daten für das Diagramm.", chlorine: "Chlor", editor_entity: "Verlaufsentität", editor_title: "Titel", editor_measurements: "Anzahl der Messungen", editor_show_co2: "CO₂ anzeigen", editor_warning: "Warnung nach (Tagen)", editor_critical: "Kritisch nach (Tagen)", editor_compact: "Kompaktmodus", editor_help_entity: "Wähle den Sensor mit dem Attribut measurements.", age_warning: "Alte Analyse", source: "Quelle"
  },
  es: {
    card_name: "JBL ProScan", card_description: "Calidad del agua e historial JBL ProScan.", title_default: "Estanque — JBL ProScan", entity_required: "Selecciona el sensor Historial JBL ProScan.", entity_missing: "Entidad no encontrada", no_data: "No hay análisis disponibles", last_analysis: "Último análisis", today: "hoy", yesterday: "ayer", days_ago: "hace {days} días", unknown_date: "fecha desconocida", good: "Bueno", warning: "Vigilar", bad: "Malo", neutral: "Información", analyses: "análisis", analysis: "análisis", history: "Historial", latest_values: "Últimas mediciones", measurements_shown: "{count} mediciones mostradas", preserved: "Se conservan los signos > y <.", local_rating: "Evaluación local configurable.", no_chart: "No hay suficientes datos para el gráfico.", chlorine: "Cloro", editor_entity: "Entidad de historial", editor_title: "Título", editor_measurements: "Número de mediciones", editor_show_co2: "Mostrar CO₂", editor_warning: "Aviso tras (días)", editor_critical: "Crítico tras (días)", editor_compact: "Modo compacto", editor_help_entity: "Selecciona el sensor cuyo atributo measurements contiene el historial.", age_warning: "Análisis antiguo", source: "Fuente"
  },
  it: {
    card_name: "JBL ProScan", card_description: "Qualità dell’acqua e storico JBL ProScan.", title_default: "Laghetto — JBL ProScan", entity_required: "Seleziona il sensore Storico JBL ProScan.", entity_missing: "Entità non trovata", no_data: "Nessuna analisi disponibile", last_analysis: "Ultima analisi", today: "oggi", yesterday: "ieri", days_ago: "{days} giorni fa", unknown_date: "data sconosciuta", good: "Buono", warning: "Da controllare", bad: "Cattivo", neutral: "Informazione", analyses: "analisi", analysis: "analisi", history: "Storico", latest_values: "Ultime misure", measurements_shown: "{count} misurazioni visualizzate", preserved: "I segni > e < vengono conservati.", local_rating: "Valutazione locale configurabile.", no_chart: "Dati insufficienti per il grafico.", chlorine: "Cloro", editor_entity: "Entità storico", editor_title: "Titolo", editor_measurements: "Numero di misurazioni", editor_show_co2: "Mostra CO₂", editor_warning: "Avviso dopo (giorni)", editor_critical: "Critico dopo (giorni)", editor_compact: "Modalità compatta", editor_help_entity: "Seleziona il sensore con l’attributo measurements.", age_warning: "Analisi datata", source: "Fonte"
  },
  nl: {
    card_name: "JBL ProScan", card_description: "Waterkwaliteit en JBL ProScan-geschiedenis.", title_default: "Vijver — JBL ProScan", entity_required: "Selecteer de JBL ProScan-geschiedenissensor.", entity_missing: "Entiteit niet gevonden", no_data: "Geen analyse beschikbaar", last_analysis: "Laatste analyse", today: "vandaag", yesterday: "gisteren", days_ago: "{days} dagen geleden", unknown_date: "datum onbekend", good: "Goed", warning: "Controleren", bad: "Slecht", neutral: "Informatie", analyses: "analyses", analysis: "analyse", history: "Geschiedenis", latest_values: "Laatste metingen", measurements_shown: "{count} metingen weergegeven", preserved: "De tekens > en < blijven behouden.", local_rating: "Configureerbare lokale beoordeling.", no_chart: "Onvoldoende gegevens voor de grafiek.", chlorine: "Chloor", editor_entity: "Geschiedenis-entiteit", editor_title: "Titel", editor_measurements: "Aantal metingen", editor_show_co2: "CO₂ tonen", editor_warning: "Waarschuwing na (dagen)", editor_critical: "Kritiek na (dagen)", editor_compact: "Compacte modus", editor_help_entity: "Selecteer de sensor met het attribuut measurements.", age_warning: "Oude analyse", source: "Bron"
  },
  pt: {
    card_name: "JBL ProScan", card_description: "Qualidade da água e histórico JBL ProScan.", title_default: "Lago — JBL ProScan", entity_required: "Selecione o sensor Histórico JBL ProScan.", entity_missing: "Entidade não encontrada", no_data: "Nenhuma análise disponível", last_analysis: "Última análise", today: "hoje", yesterday: "ontem", days_ago: "há {days} dias", unknown_date: "data desconhecida", good: "Bom", warning: "A vigiar", bad: "Mau", neutral: "Informação", analyses: "análises", analysis: "análise", history: "Histórico", latest_values: "Últimas medições", measurements_shown: "{count} medições apresentadas", preserved: "Os sinais > e < são preservados.", local_rating: "Avaliação local configurável.", no_chart: "Dados insuficientes para o gráfico.", chlorine: "Cloro", editor_entity: "Entidade de histórico", editor_title: "Título", editor_measurements: "Número de medições", editor_show_co2: "Mostrar CO₂", editor_warning: "Aviso após (dias)", editor_critical: "Crítico após (dias)", editor_compact: "Modo compacto", editor_help_entity: "Selecione o sensor cujo atributo measurements contém o histórico.", age_warning: "Análise antiga", source: "Fonte"
  }
};

function langCode(hass) {
  const raw = hass?.locale?.language || document.documentElement.lang || navigator.language || "en";
  const code = String(raw).toLowerCase().split("-")[0];
  return JBL_STRINGS[code] ? code : "en";
}
function t(hass, key, vars = {}) {
  let value = JBL_STRINGS[langCode(hass)]?.[key] ?? JBL_STRINGS.en[key] ?? key;
  for (const [name, replacement] of Object.entries(vars)) value = value.replaceAll(`{${name}}`, String(replacement));
  return value;
}

class JBLProScanCardEditor extends HTMLElement {
  constructor() { super(); this.attachShadow({ mode: "open" }); }
  set hass(value) { this._hass = value; this._render(); }
  setConfig(value) {
    this._config = { ...value };
    if (this._config.measurements == null && this._config.points != null) {
      this._config.measurements = this._config.points;
    }
    this._render();
  }
  _emit(patch) {
    this._config = { ...this._config, ...patch };
    delete this._config.points;
    this.dispatchEvent(new CustomEvent("config-changed", {
      detail: { config: this._config }, bubbles: true, composed: true
    }));
  }
  _render() {
    if (!this._hass || !this._config) return;
    const candidates = Object.values(this._hass.states)
      .filter(state => state.entity_id.startsWith("sensor.") && Array.isArray(state.attributes?.measurements))
      .sort((a, b) => (a.attributes.friendly_name || a.entity_id).localeCompare(b.attributes.friendly_name || b.entity_id));
    const options = candidates.map(state => {
      const label = state.attributes.friendly_name || state.entity_id;
      return `<option value="${state.entity_id}" ${state.entity_id === this._config.entity ? "selected" : ""}>${label}</option>`;
    }).join("");
    const count = Math.min(100, Math.max(2, Number(this._config.measurements ?? 20) || 20));
    this.shadowRoot.innerHTML = `
      <style>
        :host{display:block;color:var(--primary-text-color)}
        .help{color:var(--secondary-text-color);font-size:13px;line-height:1.4;margin:0 0 16px}
        .grid{display:grid;gap:16px}
        label{display:grid;gap:6px;font-size:14px;font-weight:500}
        input,select{box-sizing:border-box;width:100%;min-height:48px;padding:0 12px;border:1px solid var(--divider-color);border-radius:12px;background:var(--card-background-color);color:var(--primary-text-color);font:inherit}
        input:focus,select:focus{outline:2px solid var(--primary-color);outline-offset:1px}
        .switch{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:44px}
        .switch input{width:22px;min-height:22px;accent-color:var(--primary-color)}
        .two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
        @media(max-width:520px){.two{grid-template-columns:1fr}}
      </style>
      <p class="help">${t(this._hass,"editor_help_entity")}</p>
      <div class="grid">
        <label>${t(this._hass,"editor_entity")}<select id="entity"><option value=""></option>${options}</select></label>
        <label>${t(this._hass,"editor_title")}<input id="title" type="text" value="${this._config.title || ""}"></label>
        <label>${t(this._hass,"editor_measurements")}<input id="measurements" type="number" inputmode="numeric" min="2" max="100" step="1" value="${count}"></label>
        <div class="two">
          <label>${t(this._hass,"editor_warning")}<input id="warning" type="number" inputmode="numeric" min="1" max="365" step="1" value="${Number(this._config.stale_warning_days ?? 14)}"></label>
          <label>${t(this._hass,"editor_critical")}<input id="critical" type="number" inputmode="numeric" min="1" max="730" step="1" value="${Number(this._config.stale_critical_days ?? 30)}"></label>
        </div>
        <label class="switch"><span>${t(this._hass,"editor_show_co2")}</span><input id="show_co2" type="checkbox" ${this._config.show_co2 !== false ? "checked" : ""}></label>
        <label class="switch"><span>${t(this._hass,"editor_compact")}</span><input id="compact" type="checkbox" ${this._config.compact ? "checked" : ""}></label>
      </div>`;
    const listen = (id, event, fn) => this.shadowRoot.getElementById(id).addEventListener(event, e => this._emit(fn(e.target)));
    listen("entity", "change", el => ({ entity: el.value }));
    listen("title", "input", el => ({ title: el.value }));
    listen("measurements", "change", el => ({ measurements: Math.min(100, Math.max(2, Number(el.value) || 20)) }));
    listen("warning", "change", el => ({ stale_warning_days: Math.max(1, Number(el.value) || 14) }));
    listen("critical", "change", el => ({ stale_critical_days: Math.max(1, Number(el.value) || 30) }));
    listen("show_co2", "change", el => ({ show_co2: el.checked }));
    listen("compact", "change", el => ({ compact: el.checked }));
  }
}
if (!customElements.get("jbl-proscan-card-editor")) customElements.define("jbl-proscan-card-editor", JBLProScanCardEditor);

class JBLProScanCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode:"open" });
    this._selected = "ph";
  }
  static async getConfigElement() { await customElements.whenDefined("ha-form"); return document.createElement("jbl-proscan-card-editor"); }
  static getStubConfig(hass) {
    const found = hass ? Object.values(hass.states).find(s => s.entity_id.startsWith("sensor.") && Array.isArray(s.attributes?.measurements)) : null;
    return { entity:found?.entity_id || "", title:t(hass,"title_default"), measurements:20, show_co2:true, compact:false, stale_warning_days:14, stale_critical_days:30 };
  }
  setConfig(config) {
    if (!config?.entity) throw new Error(t(this._hass,"entity_required"));
    this.config = { title:null,measurements:20,show_co2:true,compact:false,stale_warning_days:14,stale_critical_days:30,...config };
    if (this.config.measurements == null && this.config.points != null) this.config.measurements = this.config.points;
  }
  set hass(value) { this._hass = value; this._render(); }
  getCardSize() { return this.config?.compact ? 8 : 12; }
  getGridOptions() { return { columns:12, rows:this.config?.compact ? 10 : 15, min_columns:4, min_rows:this.config?.compact ? 8 : 12 }; }
  _escape(value) { return String(value ?? "").replace(/[&<>\"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }
  _number(raw) { const m=String(raw??"").trim().replace(",",".").match(/^\s*([<>]=?)?\s*(-?\d+(?:\.\d+)?)/); return m?{value:Number(m[2]),comparator:m[1]||""}:{value:null,comparator:""}; }
  _locale() { return this._hass?.locale?.language || navigator.language || "en"; }
  _date(value, short=false) { const d=new Date(value); if(Number.isNaN(d.getTime())) return "—"; return new Intl.DateTimeFormat(this._locale(), short?{day:"2-digit",month:"short"}:{day:"2-digit",month:"short",year:"numeric",hour:"2-digit",minute:"2-digit"}).format(d); }
  _days(value) { const time=new Date(value).getTime(); return Number.isFinite(time)?Math.max(0,Math.floor((Date.now()-time)/86400000)):null; }
  _ageText(days) { if(days===null)return t(this._hass,"unknown_date"); if(days===0)return t(this._hass,"today"); if(days===1)return t(this._hass,"yesterday"); return t(this._hass,"days_ago",{days}); }
  _ageStatus(days) { if(days===null)return "neutral"; if(days>=Number(this.config.stale_critical_days))return "bad"; if(days>=Number(this.config.stale_warning_days))return "warning"; return "good"; }
  _defs() {
    return {
      ph:{label:"pH",unit:"",icon:"mdi:ph",status:x=>x.value===null?"neutral":x.value>=6.5&&x.value<=8.5?"good":x.value>=6&&x.value<=9?"warning":"bad"},
      kh:{label:"KH",unit:"°dKH",icon:"mdi:shield-water",status:x=>x.value===null?"neutral":x.value>=5&&x.value<=15?"good":x.value>=3&&x.value<=20?"warning":"bad"},
      gh:{label:"GH",unit:"°dGH",icon:"mdi:water-opacity",status:x=>x.value===null?"neutral":x.comparator.startsWith(">")&&x.value>=21?"warning":x.value>=4&&x.value<=21?"good":x.value>=2&&x.value<=28?"warning":"bad"},
      no2:{label:"NO₂",unit:"mg/L",icon:"mdi:alert-decagram-outline",status:x=>x.value===null?"neutral":x.comparator.startsWith(">")&&x.value>=.25?"bad":x.value===0?"good":x.value<=.25?"warning":"bad"},
      no3:{label:"NO₃",unit:"mg/L",icon:"mdi:leaf-circle-outline",status:x=>x.value===null?"neutral":x.comparator.startsWith(">")&&x.value>=50?"bad":x.value<=25?"good":x.value<=50?"warning":"bad"},
      co2:{label:"CO₂",unit:"mg/L",icon:"mdi:molecule-co2",status:()=>"neutral"},
      chlorine:{label:t(this._hass,"chlorine"),unit:"mg/L",icon:"mdi:flask-outline",status:x=>x.value===null?"neutral":x.comparator.startsWith(">")&&x.value>=.8?"bad":x.value===0?"good":x.value<=.8?"warning":"bad"}
    };
  }
  _statusText(status) { return t(this._hass,status); }
  _overall(statuses, age) { const all=[...statuses,age].filter(v=>v!=="neutral"); return all.includes("bad")?"bad":all.includes("warning")?"warning":all.length?"good":"neutral"; }
  _chart(history,key,status) {
    const limit=Math.min(100,Math.max(2,Number(this.config.measurements ?? this.config.points)||20)); const rows=history.slice(-limit);
    const values=rows.map(r=>this._number(r[key]).value); const valid=values.filter(Number.isFinite);
    if(valid.length<2)return `<div class="no-chart">${t(this._hass,"no_chart")}</div>`;
    let min=Math.min(...valid),max=Math.max(...valid); if(min===max){min-=.5;max+=.5;}
    const W=600,H=this.config.compact?120:160,px=12,py=14;
    const x=i=>px+i*(W-2*px)/Math.max(1,rows.length-1); const y=v=>py+(max-v)*(H-2*py)/(max-min);
    const segments=[]; let current=[];
    values.forEach((v,i)=>{if(Number.isFinite(v))current.push(`${x(i).toFixed(1)},${y(v).toFixed(1)}`);else if(current.length){segments.push(current);current=[];}}); if(current.length)segments.push(current);
    const lines=segments.map(s=>`<polyline points="${s.join(" ")}"/>`).join("");
    const area=segments.length===1?`<polygon points="${px},${H-py} ${segments[0].join(" ")} ${W-px},${H-py}"/>`:"";
    const lastIndex=values.map(Number.isFinite).lastIndexOf(true); const dot=lastIndex>=0?`<circle cx="${x(lastIndex)}" cy="${y(values[lastIndex])}" r="5"/>`:"";
    const firstDate=rows.find(r=>Number.isFinite(this._number(r[key]).value))?.date; const lastDate=[...rows].reverse().find(r=>Number.isFinite(this._number(r[key]).value))?.date;
    return `<div class="chart"><svg class="chart-svg s-${status}" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none"><defs><linearGradient id="jblFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="currentColor" stop-opacity=".22"/><stop offset="1" stop-color="currentColor" stop-opacity="0"/></linearGradient></defs><g class="grid"><line x1="12" y1="${H*.33}" x2="588" y2="${H*.33}"/><line x1="12" y1="${H*.66}" x2="588" y2="${H*.66}"/></g><g class="area">${area}</g><g class="line">${lines}${dot}</g></svg><div class="axis"><span>${this._date(firstDate,true)}</span><span>${t(this._hass,"measurements_shown",{count:valid.length})}</span><span>${this._date(lastDate,true)}</span></div></div>`;
  }
  _bind() {
    this.shadowRoot.querySelectorAll("button.metric").forEach(button=>button.addEventListener("click",()=>{this._selected=button.dataset.key;this._render();}));
  }
  _render() {
    if(!this._hass||!this.config)return;
    const state=this._hass.states[this.config.entity];
    if(!state){this.shadowRoot.innerHTML=`<ha-card><div class="message"><ha-icon icon="mdi:alert-circle-outline"></ha-icon>${t(this._hass,"entity_missing")}: ${this._escape(this.config.entity)}</div></ha-card>`;return;}
    const history=Array.isArray(state.attributes.measurements)?state.attributes.measurements:[];
    if(!history.length){this.shadowRoot.innerHTML=`<ha-card><div class="message"><ha-icon icon="mdi:water-alert-outline"></ha-icon>${t(this._hass,"no_data")}</div></ha-card>`;return;}
    const latest=history.at(-1),defs=this._defs();
    const keys=Object.keys(defs).filter(k=>k!=="co2"||this.config.show_co2!==false);
    if(!keys.includes(this._selected))this._selected=keys[0];
    const metrics=keys.map(key=>{const def=defs[key],raw=latest[key]??"—",status=def.status(this._number(raw));return{key,def,raw,status};});
    const ageDays=this._days(latest.date),ageStatus=this._ageStatus(ageDays),overall=this._overall(metrics.map(m=>m.status),ageStatus);
    const selected=metrics.find(m=>m.key===this._selected)||metrics[0];
    const title=this.config.title||t(this._hass,"title_default"),countLabel=history.length===1?t(this._hass,"analysis"):t(this._hass,"analyses");
    const tiles=metrics.map(m=>`<button class="metric st-${m.status} ${m.key===selected.key?"selected":""}" data-key="${m.key}" type="button"><span class="metric-top"><ha-icon icon="${m.def.icon}"></ha-icon><span class="metric-name">${m.def.label}</span><i></i></span><span class="metric-reading"><strong>${this._escape(m.raw)}</strong><small>${m.def.unit}</small></span><span class="metric-status">${this._statusText(m.status)}</span></button>`).join("");
    const integrationVersion=state.attributes.integration_version||"—";
    this.shadowRoot.innerHTML=`
      <style>
        :host{display:block;container-type:inline-size;--good:var(--success-color,#43a047);--warning:var(--warning-color,#f9a825);--bad:var(--error-color,#e53935);--neutral:var(--secondary-text-color,#757575)}
        *{box-sizing:border-box}ha-card{overflow:hidden;color:var(--primary-text-color);background:var(--ha-card-background,var(--card-background-color));border-radius:var(--ha-card-border-radius,18px)}
        .message{display:flex;align-items:center;gap:10px;padding:20px;color:var(--secondary-text-color)}
        .header{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:16px 18px 10px}.identity{display:flex;align-items:center;gap:12px;min-width:0}.hero{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;flex:none;color:var(--primary-color);background:color-mix(in srgb,var(--primary-color) 14%,transparent)}.hero ha-icon{--mdc-icon-size:25px}.title{min-width:0}.title h2{font-size:1.2rem;font-weight:500;margin:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.title p{font-size:.82rem;color:var(--secondary-text-color);margin:4px 0 0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.badge{display:flex;align-items:center;gap:7px;padding:7px 11px;border-radius:999px;background:var(--secondary-background-color);font-size:.8rem;font-weight:600;white-space:nowrap}.badge::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--neutral)}.badge.st-good::before{background:var(--good)}.badge.st-warning::before{background:var(--warning)}.badge.st-bad::before{background:var(--bad)}
        .meta{display:flex;gap:8px;padding:0 18px 14px;overflow:hidden}.chip{display:flex;align-items:center;gap:7px;min-width:0;padding:7px 10px;border-radius:12px;background:var(--secondary-background-color);font-size:.78rem}.chip ha-icon{color:var(--primary-color);--mdc-icon-size:18px}.chip span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.chip.age.st-warning,.chip.age.st-bad{color:var(--warning)}.chip.age.st-bad{color:var(--bad)}
        .section-label{padding:0 18px 8px;color:var(--secondary-text-color);font-size:.76rem;font-weight:600;text-transform:uppercase;letter-spacing:.04em}.metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;padding:0 18px 14px}.metrics:has(.metric:nth-child(6):last-child) .metric:nth-child(5){grid-column:2}.metric{appearance:none;border:1px solid transparent;background:var(--secondary-background-color);color:var(--primary-text-color);border-radius:14px;padding:10px;text-align:left;min-width:0;cursor:pointer;transition:transform .15s,border-color .15s,background .15s}.metric:hover{transform:translateY(-1px)}.metric.selected{border-color:var(--primary-color);background:color-mix(in srgb,var(--primary-color) 8%,var(--secondary-background-color))}.metric-top{display:flex;align-items:center;gap:6px}.metric-top ha-icon{--mdc-icon-size:18px;color:var(--primary-color)}.metric-name{font-size:.78rem;font-weight:600;overflow:hidden;text-overflow:ellipsis}.metric-top i{margin-left:auto;width:8px;height:8px;border-radius:50%;background:var(--neutral)}.metric.st-good i{background:var(--good)}.metric.st-warning i{background:var(--warning)}.metric.st-bad i{background:var(--bad)}.metric-reading{display:flex;align-items:baseline;gap:4px;margin-top:7px;white-space:nowrap}.metric-reading strong{font-size:1.35rem;font-weight:500}.metric-reading small{font-size:.68rem;color:var(--secondary-text-color)}.metric-status{display:block;margin-top:3px;font-size:.67rem;color:var(--secondary-text-color)}.metric.st-good .metric-status{color:var(--good)}.metric.st-warning .metric-status{color:var(--warning)}.metric.st-bad .metric-status{color:var(--bad)}
        .detail{margin:0 18px 16px;padding:14px;border-radius:16px;background:var(--secondary-background-color)}.detail-head{display:flex;align-items:flex-end;justify-content:space-between;gap:10px}.detail-title{display:flex;align-items:center;gap:9px}.detail-title ha-icon{color:var(--primary-color)}.detail-title h3{font-size:1rem;margin:0}.detail-value{display:flex;align-items:baseline;gap:5px}.detail-value strong{font-size:1.5rem;font-weight:500}.detail-value small{color:var(--secondary-text-color)}.chart{margin-top:8px}.chart-svg{width:100%;height:160px;display:block;color:var(--neutral);overflow:visible}.chart-svg.s-good{color:var(--good)}.chart-svg.s-warning{color:var(--warning)}.chart-svg.s-bad{color:var(--bad)}.chart-svg .grid line{stroke:var(--divider-color);stroke-width:1}.chart-svg .area polygon{fill:url(#jblFill)}.chart-svg .line polyline{fill:none;stroke:currentColor;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}.chart-svg .line circle{fill:currentColor;stroke:var(--card-background-color);stroke-width:3}.axis{display:flex;justify-content:space-between;color:var(--secondary-text-color);font-size:.68rem}.no-chart{height:120px;display:grid;place-items:center;color:var(--secondary-text-color);font-size:.82rem}
        .footer{display:flex;justify-content:space-between;gap:12px;padding:10px 18px 13px;border-top:1px solid var(--divider-color);font-size:.68rem;color:var(--secondary-text-color)}.versions{white-space:nowrap}
        ha-card.compact .header{padding-bottom:8px}ha-card.compact .meta{display:none}ha-card.compact .section-label{display:none}ha-card.compact .metrics{padding-top:2px}.compact .detail{padding:10px}.compact .chart-svg{height:110px}.compact .footer span:first-child{display:none}
        @container (max-width:700px){.metrics{grid-template-columns:repeat(3,minmax(0,1fr))}.metrics:has(.metric:nth-child(6):last-child) .metric:nth-child(5){grid-column:auto}}
        @container (max-width:520px){.header{align-items:flex-start}.badge{font-size:0;padding:0;background:none}.badge::before{width:11px;height:11px}.meta{flex-wrap:wrap}.chip{flex:1 1 130px}.metrics{grid-template-columns:repeat(2,minmax(0,1fr))}.detail-head{align-items:center}.footer{flex-direction:column}.versions{white-space:normal}}
        @container (max-width:360px){.metrics{grid-template-columns:1fr}.title h2{font-size:1.05rem}}
      </style>
      <ha-card class="${this.config.compact?"compact":""}">
        <div class="header"><div class="identity"><div class="hero"><ha-icon icon="mdi:water-check"></ha-icon></div><div class="title"><h2>${this._escape(title)}</h2><p>${t(this._hass,"last_analysis")}: ${this._escape(this._date(latest.date))}</p></div></div><div class="badge st-${overall}">${this._statusText(overall)}</div></div>
        <div class="meta"><div class="chip age st-${ageStatus}"><ha-icon icon="mdi:calendar-clock"></ha-icon><span>${this._ageText(ageDays)}</span></div><div class="chip"><ha-icon icon="mdi:chart-timeline-variant"></ha-icon><span>${history.length} ${countLabel}</span></div><div class="chip"><ha-icon icon="mdi:cloud-sync-outline"></ha-icon><span>${t(this._hass,"source")}: ${this._escape(latest.source||"ProScan")}</span></div></div>
        <div class="section-label">${t(this._hass,"latest_values")}</div><div class="metrics">${tiles}</div>
        <section class="detail"><div class="detail-head"><div class="detail-title"><ha-icon icon="${selected.def.icon}"></ha-icon><h3>${t(this._hass,"history")} — ${selected.def.label}</h3></div><div class="detail-value"><strong>${this._escape(selected.raw)}</strong><small>${selected.def.unit}</small></div></div>${this._chart(history,selected.key,selected.status)}</section>
        <div class="footer"><span>${t(this._hass,"preserved")} ${t(this._hass,"local_rating")}</span><span class="versions">Card v${JBL_PROSCAN_CARD_VERSION} · Integration v${this._escape(integrationVersion)}</span></div>
      </ha-card>`;
    this._bind();
  }
}
if (!customElements.get("jbl-proscan-card")) customElements.define("jbl-proscan-card", JBLProScanCard);
window.customCards=window.customCards||[];
if(!window.customCards.some(card=>card.type==="jbl-proscan-card"))window.customCards.push({type:"jbl-proscan-card",name:"JBL ProScan",description:"Water quality and JBL ProScan history",preview:true});
console.info(`%c JBL ProScan Card %c v${JBL_PROSCAN_CARD_VERSION} `,"color:white;background:#0397c5;font-weight:600;padding:2px 5px;border-radius:4px 0 0 4px","color:#0397c5;background:#e2f5fa;padding:2px 5px;border-radius:0 4px 4px 0");
