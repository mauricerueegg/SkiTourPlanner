var un=Array.isArray,on=Array.prototype.indexOf,Wn=Array.from,zn=Object.defineProperty,G=Object.getOwnPropertyDescriptor,_n=Object.getOwnPropertyDescriptors,cn=Object.prototype,vn=Array.prototype,Pt=Object.getPrototypeOf,kt=Object.isExtensible;const Jn=()=>{};function Qn(t){return t()}function Ct(t){for(var n=0;n<t.length;n++)t[n]()}const A=2,Ft=4,ot=8,mt=16,D=32,j=64,rt=128,x=256,lt=512,m=1024,P=2048,B=4096,M=8192,_t=16384,hn=32768,qt=65536,Xn=1<<17,pn=1<<19,Mt=1<<20,wt=1<<21,K=Symbol("$state"),te=Symbol("legacy props"),ne=Symbol("");function Lt(t){return t===this.v}function dn(t,n){return t!=t?n==n:t!==n||t!==null&&typeof t=="object"||typeof t=="function"}function Yt(t){return!dn(t,this.v)}function wn(t){throw new Error("https://svelte.dev/e/effect_in_teardown")}function yn(){throw new Error("https://svelte.dev/e/effect_in_unowned_derived")}function gn(t){throw new Error("https://svelte.dev/e/effect_orphan")}function En(){throw new Error("https://svelte.dev/e/effect_update_depth_exceeded")}function ee(){throw new Error("https://svelte.dev/e/hydration_failed")}function re(t){throw new Error("https://svelte.dev/e/props_invalid_value")}function mn(){throw new Error("https://svelte.dev/e/state_descriptors_fixed")}function Tn(){throw new Error("https://svelte.dev/e/state_prototype_fixed")}function xn(){throw new Error("https://svelte.dev/e/state_unsafe_mutation")}let ct=!1;function le(){ct=!0}const ae=1,se=2,fe=4,ue=8,ie=16,oe=1,_e=2,bn="[",An="[!",Rn="]",jt={},g=Symbol(),ce="http://www.w3.org/1999/xhtml";function Bt(t){console.warn("https://svelte.dev/e/hydration_mismatch")}let d=null;function Dt(t){d=t}function ve(t,n=!1,e){var r=d={p:d,c:null,d:!1,e:null,m:!1,s:t,x:null,l:null};ct&&!n&&(d.l={s:null,u:null,r1:[],r2:Tt(!1)}),Nn(()=>{r.d=!0})}function he(t){const n=d;if(n!==null){const _=n.e;if(_!==null){var e=h,r=v;n.e=null;try{for(var a=0;a<_.length;a++){var l=_[a];ft(l.effect),Y(l.reaction),$t(l.fn)}}finally{ft(e),Y(r)}}d=n.p,n.m=!0}return{}}function vt(){return!ct||d!==null&&d.l===null}function q(t,n){if(typeof t!="object"||t===null||K in t)return t;const e=Pt(t);if(e!==cn&&e!==vn)return t;var r=new Map,a=un(t),l=S(0),_=v,c=u=>{var s=v;Y(_);var f;return f=u(),Y(s),f};return a&&r.set("length",S(t.length)),new Proxy(t,{defineProperty(u,s,f){(!("value"in f)||f.configurable===!1||f.enumerable===!1||f.writable===!1)&&mn();var i=r.get(s);return i===void 0?(i=c(()=>S(f.value)),r.set(s,i)):I(i,c(()=>q(f.value))),!0},deleteProperty(u,s){var f=r.get(s);if(f===void 0)s in u&&r.set(s,c(()=>S(g)));else{if(a&&typeof s=="string"){var i=r.get("length"),o=Number(s);Number.isInteger(o)&&o<i.v&&I(i,o)}I(f,g),Ot(l)}return!0},get(u,s,f){var O;if(s===K)return t;var i=r.get(s),o=s in u;if(i===void 0&&(!o||(O=G(u,s))!=null&&O.writable)&&(i=c(()=>S(q(o?u[s]:g))),r.set(s,i)),i!==void 0){var p=V(i);return p===g?void 0:p}return Reflect.get(u,s,f)},getOwnPropertyDescriptor(u,s){var f=Reflect.getOwnPropertyDescriptor(u,s);if(f&&"value"in f){var i=r.get(s);i&&(f.value=V(i))}else if(f===void 0){var o=r.get(s),p=o==null?void 0:o.v;if(o!==void 0&&p!==g)return{enumerable:!0,configurable:!0,value:p,writable:!0}}return f},has(u,s){var p;if(s===K)return!0;var f=r.get(s),i=f!==void 0&&f.v!==g||Reflect.has(u,s);if(f!==void 0||h!==null&&(!i||(p=G(u,s))!=null&&p.writable)){f===void 0&&(f=c(()=>S(i?q(u[s]):g)),r.set(s,f));var o=V(f);if(o===g)return!1}return i},set(u,s,f,i){var Rt;var o=r.get(s),p=s in u;if(a&&s==="length")for(var O=f;O<o.v;O+=1){var tt=r.get(O+"");tt!==void 0?I(tt,g):O in u&&(tt=c(()=>S(g)),r.set(O+"",tt))}o===void 0?(!p||(Rt=G(u,s))!=null&&Rt.writable)&&(o=c(()=>S(void 0)),I(o,c(()=>q(f))),r.set(s,o)):(p=o.v!==g,I(o,c(()=>q(f))));var nt=Reflect.getOwnPropertyDescriptor(u,s);if(nt!=null&&nt.set&&nt.set.call(i,f),!p){if(a&&typeof s=="string"){var At=r.get("length"),dt=Number(s);Number.isInteger(dt)&&dt>=At.v&&I(At,dt+1)}Ot(l)}return!0},ownKeys(u){V(l);var s=Reflect.ownKeys(u).filter(o=>{var p=r.get(o);return p===void 0||p.v!==g});for(var[f,i]of r)i.v!==g&&!(f in u)&&s.push(f);return s},setPrototypeOf(){Tn()}})}function Ot(t,n=1){I(t,t.v+n)}const $=new Map;function Tt(t,n){var e={f:0,v:t,reactions:null,equals:Lt,rv:0,wv:0};return e}function S(t,n){const e=Tt(t);return en(e),e}function pe(t,n=!1){var r;const e=Tt(t);return n||(e.equals=Yt),ct&&d!==null&&d.l!==null&&((r=d.l).s??(r.s=[])).push(e),e}function I(t,n,e=!1){v!==null&&!b&&vt()&&(v.f&(A|mt))!==0&&!(y!=null&&y.includes(t))&&xn();let r=e?q(n):n;return kn(t,r)}function kn(t,n){if(!t.equals(n)){var e=t.v;Q?$.set(t,n):$.set(t,e),t.v=n,t.wv=ln(),Ut(t,P),vt()&&h!==null&&(h.f&m)!==0&&(h.f&(D|j))===0&&(T===null?jn([t]):T.push(t))}return n}function Ut(t,n){var e=t.reactions;if(e!==null)for(var r=vt(),a=e.length,l=0;l<a;l++){var _=e[l],c=_.f;(c&P)===0&&(!r&&_===h||(R(_,n),(c&(m|x))!==0&&((c&A)!==0?Ut(_,B):pt(_))))}}let L=!1;function de(t){L=t}let k;function W(t){if(t===null)throw Bt(),jt;return k=t}function we(){return W(U(k))}function ye(t){if(L){if(U(k)!==null)throw Bt(),jt;k=t}}function ge(){for(var t=0,n=k;;){if(n.nodeType===8){var e=n.data;if(e===Rn){if(t===0)return n;t-=1}else(e===bn||e===An)&&(t+=1)}var r=U(n);n.remove(),n=r}}var St,Dn,Ht,Vt;function Ee(){if(St===void 0){St=window,Dn=/Firefox/.test(navigator.userAgent);var t=Element.prototype,n=Node.prototype,e=Text.prototype;Ht=G(n,"firstChild").get,Vt=G(n,"nextSibling").get,kt(t)&&(t.__click=void 0,t.__className=void 0,t.__attributes=null,t.__style=void 0,t.__e=void 0),kt(e)&&(e.__t=void 0)}}function yt(t=""){return document.createTextNode(t)}function gt(t){return Ht.call(t)}function U(t){return Vt.call(t)}function me(t,n){if(!L)return gt(t);var e=gt(k);if(e===null)e=k.appendChild(yt());else if(n&&e.nodeType!==3){var r=yt();return e==null||e.before(r),W(r),r}return W(e),e}function Te(t,n){if(!L){var e=gt(t);return e instanceof Comment&&e.data===""?U(e):e}return k}function xe(t,n=1,e=!1){let r=L?k:t;for(var a;n--;)a=r,r=U(r);if(!L)return r;var l=r==null?void 0:r.nodeType;if(e&&l!==3){var _=yt();return r===null?a==null||a.after(_):r.before(_),W(_),_}return W(r),r}function be(t){t.textContent=""}function xt(t){var n=A|P,e=v!==null&&(v.f&A)!==0?v:null;return h===null||e!==null&&(e.f&x)!==0?n|=x:h.f|=Mt,{ctx:d,deps:null,effects:null,equals:Lt,f:n,fn:t,reactions:null,rv:0,v:null,wv:0,parent:e??h}}function Ae(t){const n=xt(t);return en(n),n}function Re(t){const n=xt(t);return n.equals=Yt,n}function Gt(t){var n=t.effects;if(n!==null){t.effects=null;for(var e=0;e<n.length;e+=1)F(n[e])}}function On(t){for(var n=t.parent;n!==null;){if((n.f&A)===0)return n;n=n.parent}return null}function Sn(t){var n,e=h;ft(On(t));try{Gt(t),n=sn(t)}finally{ft(e)}return n}function Kt(t){var n=Sn(t),e=(N||(t.f&x)!==0)&&t.deps!==null?B:m;R(t,e),t.equals(n)||(t.v=n,t.wv=ln())}function Zt(t){h===null&&v===null&&gn(),v!==null&&(v.f&x)!==0&&h===null&&yn(),Q&&wn()}function In(t,n){var e=n.last;e===null?n.last=n.first=t:(e.next=t,t.prev=e,n.last=t)}function H(t,n,e,r=!0){var a=h,l={ctx:d,deps:null,nodes_start:null,nodes_end:null,f:t|P,first:null,fn:n,last:null,next:null,parent:a,prev:null,teardown:null,transitions:null,wv:0};if(e)try{bt(l),l.f|=hn}catch(u){throw F(l),u}else n!==null&&pt(l);var _=e&&l.deps===null&&l.first===null&&l.nodes_start===null&&l.teardown===null&&(l.f&(Mt|rt))===0;if(!_&&r&&(a!==null&&In(l,a),v!==null&&(v.f&A)!==0)){var c=v;(c.effects??(c.effects=[])).push(l)}return l}function Nn(t){const n=H(ot,null,!1);return R(n,m),n.teardown=t,n}function ke(t){Zt();var n=h!==null&&(h.f&D)!==0&&d!==null&&!d.m;if(n){var e=d;(e.e??(e.e=[])).push({fn:t,effect:h,reaction:v})}else{var r=$t(t);return r}}function De(t){return Zt(),Pn(t)}function Oe(t){const n=H(j,t,!0);return(e={})=>new Promise(r=>{e.outro?qn(n,()=>{F(n),r(void 0)}):(F(n),r(void 0))})}function $t(t){return H(Ft,t,!1)}function Pn(t){return H(ot,t,!0)}function Se(t,n=[],e=xt){const r=n.map(e);return Cn(()=>t(...r.map(V)))}function Cn(t,n=0){return H(ot|mt|n,t,!0)}function Ie(t,n=!0){return H(ot|D,t,!0,n)}function Wt(t){var n=t.teardown;if(n!==null){const e=Q,r=v;Nt(!0),Y(null);try{n.call(null)}finally{Nt(e),Y(r)}}}function zt(t,n=!1){var e=t.first;for(t.first=t.last=null;e!==null;){var r=e.next;(e.f&j)!==0?e.parent=null:F(e,n),e=r}}function Fn(t){for(var n=t.first;n!==null;){var e=n.next;(n.f&D)===0&&F(n),n=e}}function F(t,n=!0){var e=!1;if((n||(t.f&pn)!==0)&&t.nodes_start!==null){for(var r=t.nodes_start,a=t.nodes_end;r!==null;){var l=r===a?null:U(r);r.remove(),r=l}e=!0}zt(t,n&&!e),it(t,0),R(t,_t);var _=t.transitions;if(_!==null)for(const u of _)u.stop();Wt(t);var c=t.parent;c!==null&&c.first!==null&&Jt(t),t.next=t.prev=t.teardown=t.ctx=t.deps=t.fn=t.nodes_start=t.nodes_end=null}function Jt(t){var n=t.parent,e=t.prev,r=t.next;e!==null&&(e.next=r),r!==null&&(r.prev=e),n!==null&&(n.first===t&&(n.first=r),n.last===t&&(n.last=e))}function qn(t,n){var e=[];Qt(t,e,!0),Mn(e,()=>{F(t),n&&n()})}function Mn(t,n){var e=t.length;if(e>0){var r=()=>--e||n();for(var a of t)a.out(r)}else n()}function Qt(t,n,e){if((t.f&M)===0){if(t.f^=M,t.transitions!==null)for(const _ of t.transitions)(_.is_global||e)&&n.push(_);for(var r=t.first;r!==null;){var a=r.next,l=(r.f&qt)!==0||(r.f&D)!==0;Qt(r,n,l?e:!1),r=a}}}function Ne(t){Xt(t,!0)}function Xt(t,n){if((t.f&M)!==0){t.f^=M,(t.f&m)===0&&(t.f^=m),X(t)&&(R(t,P),pt(t));for(var e=t.first;e!==null;){var r=e.next,a=(e.f&qt)!==0||(e.f&D)!==0;Xt(e,a?n:!1),e=r}if(t.transitions!==null)for(const l of t.transitions)(l.is_global||n)&&l.in()}}const Ln=typeof requestIdleCallback>"u"?t=>setTimeout(t,1):requestIdleCallback;let z=[],J=[];function tn(){var t=z;z=[],Ct(t)}function nn(){var t=J;J=[],Ct(t)}function Pe(t){z.length===0&&queueMicrotask(tn),z.push(t)}function Ce(t){J.length===0&&Ln(nn),J.push(t)}function It(){z.length>0&&tn(),J.length>0&&nn()}let et=!1,at=!1,st=null,C=!1,Q=!1;function Nt(t){Q=t}let Z=[];let v=null,b=!1;function Y(t){v=t}let h=null;function ft(t){h=t}let y=null;function Yn(t){y=t}function en(t){v!==null&&v.f&wt&&(y===null?Yn([t]):y.push(t))}let w=null,E=0,T=null;function jn(t){T=t}let rn=1,ut=0,N=!1;function ln(){return++rn}function X(t){var i;var n=t.f;if((n&P)!==0)return!0;if((n&B)!==0){var e=t.deps,r=(n&x)!==0;if(e!==null){var a,l,_=(n&lt)!==0,c=r&&h!==null&&!N,u=e.length;if(_||c){var s=t,f=s.parent;for(a=0;a<u;a++)l=e[a],(_||!((i=l==null?void 0:l.reactions)!=null&&i.includes(s)))&&(l.reactions??(l.reactions=[])).push(s);_&&(s.f^=lt),c&&f!==null&&(f.f&x)===0&&(s.f^=x)}for(a=0;a<u;a++)if(l=e[a],X(l)&&Kt(l),l.wv>t.wv)return!0}(!r||h!==null&&!N)&&R(t,m)}return!1}function Bn(t,n){for(var e=n;e!==null;){if((e.f&rt)!==0)try{e.fn(t);return}catch{e.f^=rt}e=e.parent}throw et=!1,t}function Un(t){return(t.f&_t)===0&&(t.parent===null||(t.parent.f&rt)===0)}function ht(t,n,e,r){if(et){if(e===null&&(et=!1),Un(n))throw t;return}e!==null&&(et=!0);{Bn(t,n);return}}function an(t,n,e=!0){var r=t.reactions;if(r!==null)for(var a=0;a<r.length;a++){var l=r[a];y!=null&&y.includes(t)||((l.f&A)!==0?an(l,n,!1):n===l&&(e?R(l,P):(l.f&m)!==0&&R(l,B),pt(l)))}}function sn(t){var p;var n=w,e=E,r=T,a=v,l=N,_=y,c=d,u=b,s=t.f;w=null,E=0,T=null,N=(s&x)!==0&&(b||!C||v===null),v=(s&(D|j))===0?t:null,y=null,Dt(t.ctx),b=!1,ut++,t.f|=wt;try{var f=(0,t.fn)(),i=t.deps;if(w!==null){var o;if(it(t,E),i!==null&&E>0)for(i.length=E+w.length,o=0;o<w.length;o++)i[E+o]=w[o];else t.deps=i=w;if(!N)for(o=E;o<i.length;o++)((p=i[o]).reactions??(p.reactions=[])).push(t)}else i!==null&&E<i.length&&(it(t,E),i.length=E);if(vt()&&T!==null&&!b&&i!==null&&(t.f&(A|B|P))===0)for(o=0;o<T.length;o++)an(T[o],t);return a!==null&&(ut++,T!==null&&(r===null?r=T:r.push(...T))),f}finally{w=n,E=e,T=r,v=a,N=l,y=_,Dt(c),b=u,t.f^=wt}}function Hn(t,n){let e=n.reactions;if(e!==null){var r=on.call(e,t);if(r!==-1){var a=e.length-1;a===0?e=n.reactions=null:(e[r]=e[a],e.pop())}}e===null&&(n.f&A)!==0&&(w===null||!w.includes(n))&&(R(n,B),(n.f&(x|lt))===0&&(n.f^=lt),Gt(n),it(n,0))}function it(t,n){var e=t.deps;if(e!==null)for(var r=n;r<e.length;r++)Hn(t,e[r])}function bt(t){var n=t.f;if((n&_t)===0){R(t,m);var e=h,r=d,a=C;h=t,C=!0;try{(n&mt)!==0?Fn(t):zt(t),Wt(t);var l=sn(t);t.teardown=typeof l=="function"?l:null,t.wv=rn;var _=t.deps,c}catch(u){ht(u,t,e,r||t.ctx)}finally{C=a,h=e}}}function Vn(){try{En()}catch(t){if(st!==null)ht(t,st,null);else throw t}}function fn(){var t=C;try{var n=0;for(C=!0;Z.length>0;){n++>1e3&&Vn();var e=Z,r=e.length;Z=[];for(var a=0;a<r;a++){var l=Kn(e[a]);Gn(l)}}}finally{at=!1,C=t,st=null,$.clear()}}function Gn(t){var n=t.length;if(n!==0)for(var e=0;e<n;e++){var r=t[e];if((r.f&(_t|M))===0)try{X(r)&&(bt(r),r.deps===null&&r.first===null&&r.nodes_start===null&&(r.teardown===null?Jt(r):r.fn=null))}catch(a){ht(a,r,null,r.ctx)}}}function pt(t){at||(at=!0,queueMicrotask(fn));for(var n=st=t;n.parent!==null;){n=n.parent;var e=n.f;if((e&(j|D))!==0){if((e&m)===0)return;n.f^=m}}Z.push(n)}function Kn(t){for(var n=[],e=t;e!==null;){var r=e.f,a=(r&(D|j))!==0,l=a&&(r&m)!==0;if(!l&&(r&M)===0){if((r&Ft)!==0)n.push(e);else if(a)e.f^=m;else{var _=v;try{v=e,X(e)&&bt(e)}catch(s){ht(s,e,null,e.ctx)}finally{v=_}}var c=e.first;if(c!==null){e=c;continue}}var u=e.parent;for(e=e.next;e===null&&u!==null;)e=u.next,u=u.parent}return n}function Zn(t){var n;for(It();Z.length>0;)at=!0,fn(),It();return n}async function Fe(){await Promise.resolve(),Zn()}function V(t){var n=t.f,e=(n&A)!==0;if(v!==null&&!b){if(!(y!=null&&y.includes(t))){var r=v.deps;t.rv<ut&&(t.rv=ut,w===null&&r!==null&&r[E]===t?E++:w===null?w=[t]:(!N||!w.includes(t))&&w.push(t))}}else if(e&&t.deps===null&&t.effects===null){var a=t,l=a.parent;l!==null&&(l.f&x)===0&&(a.f^=x)}return e&&(a=t,X(a)&&Kt(a)),Q&&$.has(t)?$.get(t):t.v}function qe(t){var n=b;try{return b=!0,t()}finally{b=n}}const $n=-7169;function R(t,n){t.f=t.f&$n|n}function Me(t){if(!(typeof t!="object"||!t||t instanceof EventTarget)){if(K in t)Et(t);else if(!Array.isArray(t))for(let n in t){const e=t[n];typeof e=="object"&&e&&K in e&&Et(e)}}}function Et(t,n=new Set){if(typeof t=="object"&&t!==null&&!(t instanceof EventTarget)&&!n.has(t)){n.add(t),t instanceof Date&&t.getTime();for(let r in t)try{Et(t[r],n)}catch{}const e=Pt(t);if(e!==Object.prototype&&e!==Array.prototype&&e!==Map.prototype&&e!==Set.prototype&&e!==Date.prototype){const r=_n(e);for(let a in r){const l=r[a].get;if(l)try{l.call(t)}catch{}}}}}export{zn as $,Se as A,he as B,me as C,ye as D,qt as E,xe as F,Ce as G,bn as H,vt as I,Pn as J,pe as K,ne as L,I as M,ce as N,Re as O,yt as P,gt as Q,Dn as R,h as S,oe as T,g as U,_e as V,Y as W,ft as X,v as Y,Nn as Z,Pe as _,we as a,un as a0,Ee as a1,U as a2,jt as a3,Rn as a4,Bt as a5,ee as a6,be as a7,Wn as a8,Oe as a9,$t as aa,K as ab,G as ac,re as ad,Xn as ae,fe as af,Yt as ag,q as ah,ue as ai,te as aj,se as ak,ae as al,ie as am,Zn as an,S as ao,Fe as ap,Ae as aq,dn as ar,Cn as b,An as c,de as d,Ne as e,Ie as f,k as g,L as h,le as i,F as j,Te as k,d as l,ct as m,Jn as n,qe as o,qn as p,De as q,ge as r,W as s,Ct as t,ke as u,Qn as v,V as w,Me as x,xt as y,ve as z};
